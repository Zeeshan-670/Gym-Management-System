from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser (AbstractUser):

    user_type = models.CharField(max_length=2,choices=(('0','Customer'),('1','Owner')),default=0)

    