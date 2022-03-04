from datetime import time

from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.views.generic import UpdateView

from Lectures.models import Lecture
from .models import Room
from .forms import RoomModelForm


# Create your views here.

def room_create_view(request):
    form = RoomModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'New room added')
        return redirect('../')
    else:
        messages.error(request, 'An error has occured')
        
    context = {
        'form' : form,
    }
    return render(request, 'Rooms/room_create.html', context)  

#Error at update and delete
def room_list_view(request):
    Rooms = Room.objects.all()  
    context = {
        'rooms': Rooms,
    }  
    if request.method =='POST':
        delete_num = request.POST.get('del_id')
        update_num = request.POST.get('upd_id', None)
        dy = request.POST.get('dy', None)
        t = request.POST.get('tm')
        if delete_num:
            print(delete_num)
            obj = Room.objects.get(id=delete_num)
            obj.delete()
            messages.success(request, 'Deleted ROom')
        elif update_num:
            print(update_num)
            obj = Room.objects.get(id=update_num)
            return redirect(f'../Room/update/{obj.id}')
        elif dy and t:
            tm = time(int(t[:2]))
            free_rooms = []
            lectures = Lecture.objects.filter(day=dy)
            for room in Rooms:
                occupied = False
                for lec in lectures:
                    if lec.start_time == tm:
                        occupied = True
                        break
                if not occupied:
                    free_rooms.append(room)
            context['freerooms'] = free_rooms
    return render(request, 'Rooms/room_list.html', context)

class RoomUpdateView(UpdateView):
    template_name = 'Rooms/room_update.html'
    form_class = RoomModelForm
    
    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Room, id=id)
    
    def form_valid(self,form):
        print(form.cleaned_data)
        form.save()
        messages.success(self.request, 'Room updated successfully.')
        return redirect('../')