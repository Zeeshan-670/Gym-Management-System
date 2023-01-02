from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import GymPackages

# Create your views here.


def Packages(request):
    package = GymPackages.objects.all()
    context = {
        'package': package
    }
    return render(request,"package.html",context)

def addPackages(request):
    return render(request,"admin/addpackage.html")

def postPackages(request):
      if request.method == "POST":
         packageprice = request.POST.get('packageprice')
         packageduration = request.POST.get('packageduration')
         packagetiming = request.POST.get('packagetiming')
         packagedays = request.POST.get('packagedays')
      if len(request.FILES) != 0:
         packagepic= request.FILES['packagepic']
         print(packagepic,packageduration,packageprice,packagetiming,packagedays)

         package = GymPackages(
           package_price = packageprice,
           package_duration = packageduration,
           package_timing = packagetiming,
           package_days = packagedays,
           package_image = packagepic,
           
          )
         print(GymPackages)
      
         package.save()
      
         return redirect('AddPackages')
         #return HttpResponse("Zain")

def PACKAGERECORDS(request):
    package = GymPackages.objects.all()
    context = {
        'package': package
    }

    return render(request,"admin/packages.html",context)
def PACKAGEEDIT(request,id):
    package= GymPackages.objects.all()

    context = {
        'package': package
    }
    
    return render(request,"admin/editpackage.html",context)