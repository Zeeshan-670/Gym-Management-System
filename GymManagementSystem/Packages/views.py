from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Packages

# Create your views here.


def Packages(request):
    return render(request,"package.html")

def addPackages(request):
    return render(request,"admin/addpackage.html")

def postPackages(request):
      if request.method == "POST":
         packageprice = request.POST.get('packageprice'),
         packageduration = request.POST.get('packageduration'),
         packagetiming = request.POST.get('packagetiming'),
         packagedays = request.POST.get('packagedays'),
         packagepic = request.FILES.get('packagepic'),

         print(packagepic)

         packagevar = Packages(
           package_price = packageprice,
           package_duration = packageduration,
           package_timing = packagetiming,
           package_days = packagedays,
           package_image = packagepic,
           
           )
         print(packagevar)
      
         packagevar.save()
      
         return redirect('AddPackages')
         return HttpResponse("Zain")

