from msilib.schema import Error
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.views.generic import UpdateView
from mysqlx import IntegrityError
from .models import Unit
from .forms import UnitModelForm


# Create your views here.

def unit_create_view(request):
    form = UnitModelForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, 'New unit created')
            return redirect('../')
        else:
            messages.error(request, 'An error has occured')
        
    context = {
        'form' : form,
    }
    return render(request, 'Units/unit_create.html', context)  

#Error at update and delete
def unit_list_view(request):
    Units = Unit.objects.all()    
    if request.method =='POST':
        delete_num = request.POST.get('del_id')
        update_num = request.POST.get('upd_id', None)
        if delete_num:
            obj = Unit.objects.get(id=delete_num)
            try:
                obj.delete()
                messages.success(request, 'Deleted Unit')
            except:
                if IntegrityError:
                    messages.error(request, "Unit has students enroled.")
                else:
                    messages.error(request, "Cannot delete unit.")
        elif update_num:
            obj = Unit.objects.get(id=update_num)
            return redirect(f'../Unit/update/{obj.id}')
    
    context = {
        'units': Units,
    }
    return render(request, 'Units/unit_list.html', context)

class UnitUpdateView(UpdateView):
    template_name = 'Units/unit_update.html'
    form_class = UnitModelForm
    
    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Unit, id=id)
    
    def form_valid(self,form):
        print(form.cleaned_data)
        form.save()
        messages.success(self.request, 'Unit updated successfully.')
        return redirect('../')