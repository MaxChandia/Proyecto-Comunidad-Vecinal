from rest_framework import serializers
from .models import User, Courses

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ('register_date', 'is_active')

class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model= Courses
        fields= '__all__'
