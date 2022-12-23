from django.db import models

# Create your models here.



class CustomAdmin(models.Model):
    
    admin_name=models.CharField(max_length=30)
    admin_email=models.CharField(max_length=30)
    admin_username=models.CharField(max_length=30)
    admin_password=models.CharField(max_length=30)