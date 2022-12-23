
from django.contrib import admin
from .models import Trainer
# Register your models here.


# @admin.register(Trainer)
# class TrainerAdmin(admin.ModelAdmin):
#     list_display=['id','trainer_name','trainer_description','trainer_image']

admin.site.register(Trainer)