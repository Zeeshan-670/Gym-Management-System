from django.db import models


# Create your models here.
class GymProducts(models.Model):
    
    name=models.CharField(max_length=30)
    price=models.CharField(max_length=30)  
    oldprice=models.CharField(max_length=30)
    description=models.CharField(max_length=100)
    image=models.ImageField(upload_to="productimage")

class Order(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postcode = models.IntegerField()
    email = models.EmailField(max_length=100)
    phone = models.IntegerField()
    additional_info = models.TextField()
    amount = models.CharField(max_length=100)


class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    product = models.CharField(max_length=200)
    image = models.ImageField(upload_to="productimage/OrderImage")
    quantity = models.CharField(max_length=20)
    price = models.CharField(max_length=50)
    total = models.CharField(max_length=1000)


    def __str__(self):
        return self.order.user.username
