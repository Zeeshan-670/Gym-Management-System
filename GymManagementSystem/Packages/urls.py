from django.urls import path,include
from . import views

urlpatterns = [
    path('packages/',view=views.Packages,name="Packages"),


    #Admin
    path('addpackages/',view=views.addPackages,name="AddPackages"),
    path('postpackages/',view=views.postPackages,name="postAddPackage"),
    path('packagerecords/',view=views.PACKAGERECORDS,name="packagerecords"),
    path('packagerecords/<str:id>',view=views.PACKAGEEDIT,name="EditPackages")

]
