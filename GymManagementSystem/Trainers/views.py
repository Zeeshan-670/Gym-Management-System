from django.shortcuts import render,redirect
from .models import Trainer
from django.http import HttpResponse

# Create your views here.


def trainers(request):
    return render(request,'user/trainers.html')
    

def addTrainers(request):


    return render(request,'admin/addtrainer.html')    

def PostaddTrainer(request):
    print(request)
    if request.method == "POST":
      trainername = request.POST.get('trainername'),
      trainerdescription = request.POST.get('trainerdescription'),
      trainerimage = request.FILES.get('trainerimage'),

      print(trainerimage)

      trainervar = Trainer(
           trainer_name = trainername,
           trainer_description = trainerdescription,
           trainer_image = trainerimage,
           
        )
      print(trainervar)
      
      trainervar.save()
      
      return redirect('')

     





