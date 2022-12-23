from django.db import models

# Create your models here.

class Trainer(models.Model):
    
    trainer_name=models.CharField(max_length=30)
    trainer_description=models.CharField(max_length=30)
    trainer_image=models.ImageField(upload_to="trainerimage")