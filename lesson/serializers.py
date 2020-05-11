from rest_framework import serializers
from .models import Teacher, Lesson

class FitnessSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('name', 'description', 'startTime', 'endTime', 'place', 'weekDay',
                  'appointment_id', 'teacher_v2', 'service_id', 'pay', 'color', 'availability')
