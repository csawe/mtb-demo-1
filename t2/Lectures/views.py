from datetime import time

from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.views.generic import UpdateView
from pyparsing import one_of

from Lectures.models import Lecture
from Rooms.models import Room, Time

from .form import LectureModelForm

# Create your views here.

def lecture_create_view(request):
    form = LectureModelForm(request.POST or None)
    if form.is_valid():
        #room_id = form.cleaned_data.get('room')
        #time_occupied = form.cleaned_data.get('start_time')
        #room = Room.objects.get(room_id=room_id)
        #room.time_occupied.add(Time.objects.get(time_occupied=time_occupied))
        
        room_id = form.cleaned_data.get('room')
        time_occupied = form.cleaned_data.get('start_time')
        lectures = Lecture.objects.all()
        occupied = False
        for lec in lectures:
            if lec.room == room_id and lec.start_time == time_occupied:
                occupied = True
        if occupied==False:
            form.save()
            messages.success(request, 'Lecture added successfuly')
            return redirect('../Lecture/master')
        else:
            messages.error(request, 'Room is occupied at that time')
    else:
        messages.error(request, 'An error occured')
    context = {
        'form': form,
    }
    return render(request, 'Lectures/lecture_create.html', context)


class timestamp():
    def __init__(self, hr):
        self.time = time(hr, 0, 0)
timestamps = [timestamp(7), timestamp(8), timestamp(9), timestamp(10), timestamp(11), timestamp(12), timestamp(13), timestamp(14), timestamp(15), timestamp(16), timestamp(17)]

class day():
    def __init__(self, d):
        self.d = d
days = [day('monday'), day('tuesday'),day('wednesday'), day('thursday'), day('friday')]



def lecture_list_view(request):
    rooms = Room.objects.all()
    lectures = Lecture.objects.all()
    context = {
        'lectures' : lectures,
        'rooms' : rooms,
        'time' : timestamps,
        'days' : days,
    }
    return render(request, 'Lectures/lecture_master_timetable.html', context)

def lecture_student_view(request):
    rooms = Room.objects.all()
    lectures = Lecture.objects.all()
    context = {
        'time' : timestamps,
        'days':days,
        'rooms':rooms,
        'lectures':lectures,
    }
    return render(request, 'Lectures/lecture_student_timetable.html', context)

class LectureUpdateView(UpdateView):
    template_name = 'Departments/department_update.html'
    form_class = LectureModelForm
    
    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Lecture, id=id)
    
    def form_valid(self,form):
        print(form.cleaned_data)
        form.save()
        messages.success(self.request, 'Lecture updated successfully.')
        return redirect('../')