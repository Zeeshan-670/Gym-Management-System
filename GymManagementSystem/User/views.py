from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.


def signin(request):
    return render(request,'signin.html')

def signup(request):
    return render(request,'signup.html')

def register(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname'),
        lastname = request.POST.get('lastname'),
        email = request.POST.get('email'),       
        username=request.POST.get('username'),
        password = request.POST.get('password')   

        
        if User.objects.filter(email = email).exists():
             messages.error(request,'email id are already exists')
             return redirect('signup')


        user = User(
           first_name= firstname,
           last_name= lastname,
           email = email,
           username = username
        )
        user.set_password(password)
        user.save()
        return redirect('signin')
        #  firstname=request.POST['firstname'],
        #  lastname=request.POST['lastname'],
        #  email=request.POST['email'],       
        #  phone=request.POST['phone'],
        #  password=request.POST['password'],       
        #  repeat_password=request.POST['repeat_password'],  
       
    #    user=User(firstname,lastname,email,phone,password,repeat_password),
    #    user.Save()

# def login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username'),
#         password = request.POST.get('password'),

#         user = authenticate(request,username = username, password = password)
#         print(user)
#         if user is not None:
#            # messages.error(request,'Login Failed')
#             login(request,user)
#             return redirect('index')
#         else:
#             return redirect('login')        

#     return render(request,"signin.html")
         
def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        user = authenticate(request,username = username, password = password)
        if user is not None and user.is_active:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, 'Email and Password are invalid !')
        return redirect('login')   

    return render(request,"signin.html")    



