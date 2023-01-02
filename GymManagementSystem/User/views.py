from django.shortcuts import render,redirect
from django.http import HttpResponse
from User.models import CustomUser
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.


def signin(request):
    return render(request,'signin.html')

def signup(request):
    return render(request,'signup.html')

def register(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')       
        username=request.POST.get('username')
        password = request.POST.get('password')   

        
        # if User.objects.filter(email = email).exists():
        #      messages.error(request,'email id are already exists')
        #      return redirect('signup')


        user = CustomUser(
           first_name= firstname,
           last_name= lastname,
           email = email,
           username = username
        )
        user.set_password(password)
        user.save()
        return redirect('handlelogin')
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
   
 return render(request,"signin.html")    



def dologin (request):
      if request.method == "POST":
        user= authenticate(request,
        username=request.POST.get('username'),
        password=request.POST.get('password'))

        if user!=None:
            login(request,user)
            user_type = user.user_type
            if user_type == '0':
                return redirect('home')
            elif user_type == '1':
                return redirect('adminhome')
        else:
            messages.error(request,'Fields Not Matched!')
            return redirect('handlelogin')
      else:
         messages.error(request,'Fields Not Matched!')
         return redirect('handlelogin')             


#Portfolio Work

def PROFILE(request):
    #return HttpResponse("<h1>Portfolio</h1>")
    return render(request,'profile.html')

def PROFILE_UPDATE(request):
    if request.method == "POST":
        
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user_id = request.user.id
        

        user = CustomUser.objects.get(id = user_id)
        user.first_name = first_name    
        user.last_name = last_name
        user.username = username
        user.email = email
    

        if password != None and password != "":
            user.set_password(password)

        user.save()
        
        messages.success(request,'Profile updated Successfully')
        return redirect('profile')


#Dashboard

def DASHBOARD(request):
    return render(request,"dashboard.html")