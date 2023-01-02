from django.urls import path,include
from . import views


urlpatterns = [
     #  Trainer Url For Website
     path('trainers/',view=views.trainers,name="trainers"),

     #Trainer Url For Admins
     path('addtrainer/',view=views.addTrainers,name="addtrainer"),
     path('traineradd/',view=views.PostaddTrainer,name="postAddTrainer"),
     path('trainerrecords/',view=views.TRAINERRECORDS,name="trainerrecords"),
     path('trainerrecords/<str:id>',view=views.TRAINEREDIT,name="EditTrainer"),
     path('update/<str:id>',view=views.UPDATETRAINER,name="update"),
     path('delete/<str:id>',view=views.DELETETRAINER,name="delete")
]
