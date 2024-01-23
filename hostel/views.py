from django.shortcuts import render
from .models import *
from django.http import HttpResponse
# Create your views here.

def view(request):
    return render(request,"hostel/view.html")
     
def add_student(request):
    if request.method == 'POST':
        adm_no = request.POST.get('adm_no')
        name = request.POST.get('name')
        email = request.POST.get('email')
        pgm_id = request.POST.get('pgm_id')

        student = Student(adm_no=adm_no,name=name,email=email,pgm_id=pgm_id)
        student.save()

        return HttpResponse("<h1 align='center'>Student added</h1>")
    return render(request,"hostel/fstudent.html")

def get_student(request):
    s_get={
        'stud':Student.objects.all()
    }
    return render(request,'hostel/student.html',s_get)

def add_room(request):
    if request.method == 'POST':
        room_id = request.POST.get('room_id')
        room_no = request.POST.get('room_no')
        floor = request.POST.get('floor')
        capacity = request.POST.get('capacity')

        room = Rooms(room_id=room_id,room_no=room_no,floor=floor,capacity=capacity)
        room.save()

        return HttpResponse("<h1>Room added Successfully</h1>")
    return render(request,'hostel/froom.html')

def get_room(request):
    r_get={
        'room':Rooms.objects.all()
    }
    return render(request,'hostel/room.html',r_get)

def add_dept(request):
    if request.method == "POST":
        dept_id = request.POST.get('dept_id')
        dept_name = request.POST.get('dept_name')

        department = Department(dept_id=dept_id,dept_name=dept_name)
        department.save()

        return HttpResponse("<h1>Department added successfully</h1>")
    return render(request,'hostel/fdept.html')

def get_dept(request):
    d_get={
        'dept':Department.objects.all()
    }
    return render(request,'hostel/dept.html',d_get)

def add_attendance(request):
    if request.method == 'POST':
        adm_no = request.POST.get('adm_no')
        date = request.POST.get('date')

        attendance = Attendance(adm_no=adm_no,date=date)
        attendance.save()
        return HttpResponse("<h1 align='center'>Attendance Submitted</h1>")
    return render(request,"hostel/fatd.html")

def get_attendance(request):
    a_get = {
        'attendance':Attendance.objects.all()
    }
    return render(request,"hostel/atd.html",a_get)
