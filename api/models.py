from django.db import models

class User (models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=100)
    register_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)


class Courses(models.Model):
    course_name = models.CharField(max_length=100)

class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    
class Evaluations(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    evaluation_score = models.FloatField()

class Activities(models.Model):
    activity_name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, default='Descripción no disponible')
    register_date = models.DateTimeField(auto_now_add=True, default= 'día no disponible')
    
