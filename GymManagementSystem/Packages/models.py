from django.db import models

# Create your models here.


class Packages(models.Model):
    
    package_price=models.CharField(max_length=30)
    package_duration=models.CharField(max_length=50)
    package_timing=models.CharField(max_length=90)
    package_days=models.CharField(max_length=200)
    package_image=models.ImageField(upload_to="packageimage")