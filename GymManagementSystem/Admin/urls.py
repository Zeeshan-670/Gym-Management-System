from django.urls import path,include
from . import views


urlpatterns = [
    path('adminhome/',view=views.home,name="adminhome"),
    path('newtrainer/',view=views.newtrainer,name="newtrainer"),

    #Admin Login
    # path('adminlogin/',view=views.AdminLogin,name="adminlogin"),
]
