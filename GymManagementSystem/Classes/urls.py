from django.contrib import admin
from django.urls import path,include
from . import views



urlpatterns = [
    path('classes/',view=views.classes,name="classes"),
]
