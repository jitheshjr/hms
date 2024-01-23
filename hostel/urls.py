from django.urls import path
from . import views 

urlpatterns = [
    path("",views.view),
    path("add",views.add_student,name='add_student'),
    path("get",views.get_student,name='get_student'),
    path("room",views.add_room,name='add_room'),
    path("getroom",views.get_room,name='get_room'),
    path("dept",views.add_dept,name='add_dept'),
    path("getdept",views.get_dept,name='get_dept'),
    path("addatd",views.add_attendance,name='add_attendance'),
    path("getatd",views.get_attendance,name='get_attendance')
]
