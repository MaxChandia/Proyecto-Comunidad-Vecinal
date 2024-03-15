from django.urls import path, include
from api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'courses', views.CoursesViewSet)


urlpatterns = [
    path('', include(router.urls))
]