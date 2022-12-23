from django.urls import path,include
from . import views


urlpatterns = [
    path('home/',view=views.home,name="home"),
    path('newtrainer/',view=views.newtrainer,name="newtrainer"),

    #Admin Login
    path('adminlogin/',view=views.AdminLogin,name="adminlogin"),
]
