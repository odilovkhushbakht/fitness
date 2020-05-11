from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='image/')
    position = models.CharField(max_length=255)

class Lesson(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    teacher_name = models.CharField(max_length=50)
    startTime = models.TimeField()
    endTime = models.TimeField()
    place = models.CharField(max_length=100)
    pay = models.BooleanField()
    appointment_id = models.CharField(max_length=100)
    service_id = models.CharField(max_length=100)
    weekDay = models.IntegerField()
    color = models.CharField(max_length=7)
    availability = models.IntegerField()
    teacher_v2 = models.ForeignKey('teacher', on_delete=models.CASCADE)