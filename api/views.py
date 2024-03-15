from rest_framework import viewsets
from .serializer import UserSerializer, CoursesSerializer
from .models import User, Courses, Activities

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CoursesViewSet(viewsets.ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer
    

