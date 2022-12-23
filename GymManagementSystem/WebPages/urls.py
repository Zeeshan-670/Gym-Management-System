from django.urls import path,include
from . import views


urlpatterns = [
     path('aboutus/',view=views.aboutus,name="aboutus"),
     path('contactus/',view=views.contactus,name="contactus"),
     path('post/contact',view=views.PostContact,name="postcontact")
]
