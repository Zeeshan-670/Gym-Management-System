from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.contrib.auth.models import User
# from . models import CustomAdmin
# from django.contrib import messages
# from django.contrib.auth import authenticate,login,logout

# Create your views here.



def home(request):
    #return HttpResponse("Zain")
     return render(request,"adminhome.html")

def newtrainer(request):
    return render(request,"addtrainer.html")    
def USERS(request):
    #  users = User.objects.all()
    #  context = {
    #     'users': users
    #  }
     return render(request,"users.html")