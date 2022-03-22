from datetime import time, datetime, date
import calendar

from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from django.views.generic import UpdateView

from Lectures.models import Lecture
from Rooms.models import Room

from .form import LectureModelForm

# Create your views here.

def update_lectures():
    print("Checking...")
    lectures = Lecture.objects.all()
    date_today = date.today()
    time_today = datetime.now()
    for lecture in lectures:
        if ((lecture.day == calendar.day_name[date_today.weekday()]) and (lecture.dateCreated.date != time_today.date())) or (lecture.day != calendar.day_name[date_today.weekday()]):
            if lecture.reason != "lecture":
                check_time = lecture.start_time.hour + lecture.duration        
                if lecture.day == calendar.day_name[date_today.weekday()]:
                    if check_time >= 17:
                        lecture.delete()
            ##Edit check and enable deleting.
            #17 is the end of the day
            #At the end of the day each lesson is checked.    
            
update_lectures()       

def lecture_create_view(request):
    form = LectureModelForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            room_id = form.cleaned_data.get('room')
            time_occupied = form.cleaned_data.get('start_time')
            day = form.cleaned_data.get('day')
            lectures = Lecture.objects.all()
            occupied = False
            for lec in lectures:
                if lec.room == room_id and lec.start_time == time_occupied and lec.day == day:
                    occupied = True
            if occupied==False:
                unit = form.cleaned_data.get('unit')
                department = form.cleaned_data.get('department')
                lecturer = form.cleaned_data.get('lecturer')
                duration = form.cleaned_data.get('duration')
                start_time = form.cleaned_data.get('start_time')
                if duration>3 or duration<1:
                    messages.error(request, 'Lectures cannot be more that three hours')
                elif (start_time.hour < 7) or (start_time.hour > 16):
                    messages.error(request, 'Lecture is outside learning hours')
                else:
                    form.save()    
                    if duration==2:
                        Lecture.objects.create(unit=unit, lecturer=lecturer, department=department, room=room_id, day=day, start_time=time_occupied.replace(hour=time_occupied.hour+1) ,duration=1)    
                    elif duration>2 and duration<4:
                        Lecture.objects.create(unit=unit, lecturer=lecturer, department=department, room=room_id, day=day, start_time=time_occupied.replace(hour=time_occupied.hour+1) ,duration=1)
                        Lecture.objects.create(unit=unit, lecturer=lecturer, department=department, room=room_id, day=day, start_time=time_occupied.replace(hour=time_occupied.hour+2) ,duration=1)
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
days = [day('Monday'), day('Tuesday'),day('Wednesday'), day('Thursday'), day('Friday')]

groups = ['student','lecturer']
    
'''
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
'''


def room_detail_view(request):
    update_lectures() 
    rooms = Room.objects.all()
    lectures = Lecture.objects.all()
    context = {
        'lectures':lectures,
        'rooms':rooms,
        'time' : timestamps,
        'days' : days
    }
    if request.method == "POST":
        r = request.POST.get('dy',None)
        if r:
            r_id = Room.objects.get(room_id=r)
            context['rid'] = r_id
        else:
            print("No room chosen")
    
    return render(request, 'Lectures/master_timetable.html', context)    

def lecture_student_view(request):
    update_lectures() 
    rooms = Room.objects.all()
    lectures = Lecture.objects.all()
    context = {
        'time' : timestamps,
        'days':days,
        'rooms':rooms,
        'lectures':lectures,
        'groups':groups,
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