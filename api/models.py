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
    

class Neighborhood_Headquarters(models.Model):
    schedule = models.CharField(max_length=100)

class Activities(models.Model):
    activity_name = models.CharField(max_length=100)
