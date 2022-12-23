from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import ContactUs
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.


def aboutus(request):
    return render(request,'aboutus.html')

def contactus(request):
    return render(request,'contactus.html')
def PostContact(request):
     if request.method == 'POST':
        name = request.POST.get('name'),
        email = request.POST.get('email'),
        number = request.POST.get('phone_number'),       
        subject=request.POST.get('subject'),
        message = request.POST.get('message')   

        
        # if ContactUs.objects.filter(email = email).exists():
        #      messages.error(request,'email id are already exists')
        #      return redirect('contactus')


        contactus = ContactUs(
           guest_name= name,
           guest_email= email,
           guest_phone = number,
           guest_subject = subject,
           guest_message =message
        )
        contactus.save()
        return redirect('contactus')
    #return render(request,'contactus.html')




