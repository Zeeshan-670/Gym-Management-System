from django.urls import path,include
from . import views


urlpatterns = [
     # path('signin/',view=views.signin,name="signin"),
     path('signup/',view=views.signup,name="signup"),
     path('register/',view=views.register,name="register"),
     path('accounts/login/',view=views.Login,name="handlelogin"),
     path('accounts/',include('django.contrib.auth.urls')),
     path('dologin/',view=views.dologin,name="dologin"),
  

     #Profile Work

     
     path('profile/',view=views.PROFILE,name="profile"),
     path('profile_update',view=views.PROFILE_UPDATE,name="profile_update"),


     path('dashboard/',view=views.DASHBOARD,name="dashboard"),



]
