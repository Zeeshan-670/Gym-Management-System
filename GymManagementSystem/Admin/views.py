from django.shortcuts import render,redirect
from django.http  import HttpResponse
# from . models import CustomAdmin
# from django.contrib import messages
# from django.contrib.auth import authenticate,login,logout

# Create your views here.



def home(request):
    #return HttpResponse("Zain")
     return render(request,"adminhome.html")

def newtrainer(request):
    return render(request,"addtrainer.html")    

# def AdminLogin(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         print(username,password)
#         CustomAdmin = authenticate(request,username = username, password = password)

#         print(CustomAdmin)
#         if CustomAdmin is not None and CustomAdmin.is_active:
#             login(request,CustomAdmin)
#             return redirect('home')
#         else:
#             messages.error(request, 'Email and Password are invalid !')
#         return redirect('adminlogin')   

#     #return HttpResponse("Zain")
#     return render(request,"adminsignin.html")
