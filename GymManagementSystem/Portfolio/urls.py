from django.contrib import admin
from django.urls import path,include
from . import views



urlpatterns = [
    path('portfolio/',view=views.portfolio,name="portfolio")
]
