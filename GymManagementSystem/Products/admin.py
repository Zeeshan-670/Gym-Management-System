from django.contrib import admin
from .models import GymProducts,Order,OrderItem
# Register your models here.

class OrderItemTubleInline(admin.TabularInline):
    model = OrderItem

class OrderAdmin(admin.ModelAdmin):
    inlines =[OrderItemTubleInline]    

admin.site.register(GymProducts)


admin.site.register(Order,OrderAdmin)

admin.site.register(OrderItem)
