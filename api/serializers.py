from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model =Student
        fields= ['id','name','roll','city']

    def validate_roll(self,value):
        if Student.objects.filter(roll=value).exists():
            raise serializers.ValidationError('Roll already exists')
        return value