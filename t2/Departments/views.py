from datetime import datetime

from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.views.generic import UpdateView

from Lectures.models import Lecture
from Lectures.views import timestamps, days

from .models import Department
from .forms import DepartmentModelForm


# Create your views here.

def department_create_view(request):
    form = DepartmentModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'New department created')
        return redirect('../Department')
    else:
        messages.error(request, 'An error has occured')
        
    context = {
        'form' : form,
    }
    return render(request, 'Departments/department_create.html', context)
    

def department_list_view(request):
    Departments = Department.objects.all()
    d = datetime.today().strftime('%A').lower()
    now = datetime.now()
    t = now.strftime('%H:%M:%S')
    h = t[:2]
    lectures = Lecture.objects.filter(day=d, start_time=str(h)+':0')
    if request.method =='POST':
        del_num = request.POST.get('delete_id', None)
        upd_num = request.POST.get('update_id', None)
        if del_num:
            obj = Department.objects.get(id=del_num)
            obj.delete()
            messages.success(request, 'Deleted department')
        elif upd_num:
            obj = Department.objects.get(id=upd_num)
            return redirect(f'../Department/update/{obj.id}')
    
    context = {
        'departments': Departments,
        'lectures' : lectures,
    }
    return render(request, 'Departments/department_list.html', context)

class DepartmentUpdateView(UpdateView):
    template_name = 'Departments/department_update.html'
    form_class = DepartmentModelForm
    
    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Department, id=id)
    
    def form_valid(self,form):
        print(form.cleaned_data)
        form.save()
        messages.success(self.request, 'Department updated successfully.')
        return redirect('../')