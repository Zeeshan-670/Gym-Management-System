from django.db import models

# Create your models here.




class ContactUs(models.Model):
    
    guest_name=models.CharField(max_length=30)
    guest_email=models.CharField(max_length=30)
    guest_phone=models.CharField(max_length=30)
    guest_subject=models.CharField(max_length=30)
    guest_message=models.TextField(max_length=1000)