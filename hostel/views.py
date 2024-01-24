from django.shortcuts import render
from .models import *
from django.http import HttpResponse
# Create your views here.

#home page 
def view(request):
    return render(request,"hostel/view.html")
     
#adding student to Student model     
def add_student(request):
    if request.method == 'POST':
        #retrieve data from POST request
        adm_no = request.POST.get('adm_no')
        name = request.POST.get('name')
        email = request.POST.get('email')
        pgm_id = request.POST.get('pgm_id')

        #creating a instance of Student
        student = Student(adm_no=adm_no,name=name,email=email,pgm_id=pgm_id)
        #saving instance to database
        student.save()

        return HttpResponse("<h1 align='center'>Student added</h1>")
    return render(request,"hostel/fstudent.html")#if method is not post 

#retrieving data from Student model
def get_student(request):
    s_get={
        'stud':Student.objects.all()
    }
    return render(request,'hostel/student.html',s_get)

#adding room to Rooms model
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

#retrieving data from Rooms model
def get_room(request):
    r_get={
        'room':Rooms.objects.all()
    }
    return render(request,'hostel/room.html',r_get)

#Adding data to Department model
def add_dept(request):
    if request.method == "POST":
        dept_id = request.POST.get('dept_id')
        dept_name = request.POST.get('dept_name')

        department = Department(dept_id=dept_id,dept_name=dept_name)
        department.save()

        return HttpResponse("<h1>Department added successfully</h1>")
    return render(request,'hostel/fdept.html')

#retrieving data from Department model
def get_dept(request):
    d_get={
        'dept':Department.objects.all()
    }
    return render(request,'hostel/dept.html',d_get)

#adding attendance to Attendance model
def add_attendance(request):
    if request.method == 'POST':
        adm_nos = request.POST.getlist('adm_no')
        date = request.POST.get('date')

        for adm_no in adm_nos:
            attendance = Attendance(adm_no=adm_no,date=date)
            attendance.save()
        return HttpResponse("<h1 align='center'>Attendance Submitted</h1>")
    return render(request,"hostel/fatd.html")

#retrieving attendance report from Attendance model
def get_attendance(request):
    a_get = {
        'attendance':Attendance.objects.all()
    }
    return render(request,"hostel/atd.html",a_get)
