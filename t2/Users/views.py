from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.views.generic import UpdateView


from .forms import NewUserForm, UpdateUserForm
from .models import NewUser

# Create your views here.
def home(request):
    context = {}
    return render(request, 'Users/home.html', context)

def user_registration_view(request):
    form = NewUserForm(request.POST or None)
    if form.is_valid():
        print("In here")
        form.save()
        print("Still here")
        username = form.cleaned_data.get('username')
        user = NewUser.objects.get(username=username)
        user.is_active = True
        user.save()
        messages.success(request, 'Registration Successfull')
        return redirect('../../')

    context = {
        'form' : form,
    }
    return render(request, 'Users/user_registration.html', context)

def user_login_view(request):  
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            uname = form.cleaned_data.get('username')
            pwd = form.cleaned_data.get('password')
            user = authenticate(username=uname, password=pwd)
            if user is not None:
                person = NewUser.objects.get(username=uname)
                person.is_active = True
                 
                login(request, user)
                messages.info(request, f'You are now logged in as {uname}')
                return redirect('../../')
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, 'Enter valid details')
    form = AuthenticationForm()
    context = {
        'form':form,
    }
    return render(request, 'Users/user_login.html', context)

def user_logout_view(request):
    logout(request)
    messages.info(request, 'You have successfully logged out')
    return redirect('../../')

class UserUpdateView(UpdateView):
    template_name = 'Users/user_update.html'
    form_class = UpdateUserForm
    
    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(NewUser, id=id)
    
    def form_valid(self,form_class):
        print(form_class.cleaned_data)
        form_class.save()
        messages.success(self.request, 'Log in details updated successfully.')
        return redirect('../../')
    
def UserUpdateView2(request):
    form = NewUserForm(request.POST or None)
    user = NewUser.objects.get(id= request.user.id)
    if form.is_valid():
        form.save()
        messages.success(request, 'Log in details updated successfully.')
        return redirect('../')
        
    context = {
        'form' : form
    }
    return render(request, 'Units/unit_update.html', context)