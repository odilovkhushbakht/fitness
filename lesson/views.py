from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Lesson, Teacher
from .serializers import FitnessSerializers

# Create your views here.

class LessonList(APIView):

    def get(self,request):
        lesson = Lesson.objects.all()
        serializer = FitnessSerializers(lesson, many=True)
        data = serializer.data
        size = serializer.data.__len__()
        for item in range(0,size):
            teacher_v2 = Teacher.objects.filter(id=data[item]['teacher_v2']).values('name', 'short_name', 'image', 'position')
            data[item]['teacher_v2'] = teacher_v2
        return Response(serializer.data)