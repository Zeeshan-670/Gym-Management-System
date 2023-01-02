from django.shortcuts import render,redirect
from .models import Trainer
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.


def trainers(request):
     trainer = Trainer.objects.all()
     context = {
        'trainer': trainer
     }

     return render(request,'user/trainers.html',context)
    

def addTrainers(request):

  return render(request,"admin/addtrainer.html")    

def PostaddTrainer(request):
    print(request)
    if request.method == "POST":
      trainername = request.POST.get('trainername')
      trainerdescription = request.POST.get('trainerdescription')
      if len(request.FILES) != 0:
        trainerimage= request.FILES['trainerimage']

      print(trainerimage,trainername,trainerdescription)

      trainervar = Trainer(
           trainer_name = trainername,
           trainer_description = trainerdescription,
           trainer_image = trainerimage,
           
        )
      print(trainervar)
      
      trainervar.save()
      
      return redirect('adminhome')

def TRAINERRECORDS(request):
  trainer = Trainer.objects.all()
  context = {
        'trainer': trainer
    }
  return render(request,"admin/trainers.html",context)    

def TRAINEREDIT(request,id):
   trainer = Trainer.objects.filter(id = id)
   context = {
        'trainer':trainer,
    }

   return render(request,"admin/edittrainer.html",context)
     
def UPDATETRAINER(request,id):
    print(request)
    if request.method == "POST":
      trainername = request.POST.get('trainername')
      trainerdescription = request.POST.get('trainerdescription')
      if len(request.FILES) != 0 :
        trainerimage= request.FILES['trainerimage']


      trainervar = Trainer(
           id = id,
           trainer_name = trainername,
           trainer_description = trainerdescription,
           trainer_image = trainerimage,
           
        )
      print(trainervar)
      
      trainervar.save()

    return redirect("trainerrecords")

def DELETETRAINER(request,id):
   trainer = Trainer.objects.get(id = id)
   trainer.delete()
   messages.success(request,'Trainer Deleted Successfully')
   return redirect('trainerrecords')

   #return redirect(trainerrecords)   




