from django.urls import path
from . import views

urlpatterns = [
    path('courseone', views.courseone),
    path('coursetwo', views.coursetwo),
]