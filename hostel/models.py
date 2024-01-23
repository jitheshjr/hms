from django.db import models

# Create your models here.
class Student(models.Model):
    adm_no = models.IntegerField()
    name = models.CharField(max_length=42)
    email = models.CharField(max_length=42)
    pgm_id = models.IntegerField()

class Rooms(models.Model):
    room_id = models.IntegerField()
    room_no = models.IntegerField()
    floor = models.IntegerField()
    capacity = models.IntegerField()

class Department(models.Model):
    dept_id = models.IntegerField()
    dept_name = models.CharField(max_length=42)

class Attendance(models.Model):
    adm_no = models.IntegerField()
    date = models.DateField()