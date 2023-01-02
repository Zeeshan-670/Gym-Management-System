from django.shortcuts import render,redirect
from .models import GymProducts,Order
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from django.shortcuts import get_list_or_404, get_object_or_404
from django.http import HttpResponse
# Create your views here.


def Products(request):
    products= GymProducts.objects.all()

    context = {
        'products': products
    }
    return render(request,"products.html",context)


#Admin Panel Work

def ADDPRODUCTS(request):
    return render(request,"admin/addproducts.html")    

def POSTADDPRODUCT(request):
    print(request)
    if request.method == "POST":
      productname = request.POST.get('productname')
      productprice = request.POST.get('productprice')
      productoldprice = request.POST.get('productoldprice')
      productdescription = request.POST.get('productdescription')
      if len(request.FILES) != 0:
        productimage= request.FILES['productimage']

      products = GymProducts(
           product_name = productname,
           product_price = productprice,
           product_oldprice = productoldprice,
           product_description = productdescription,
           product_image = productimage
           
        )
      
      products.save()
      
    return render(request,"admin/addproducts.html")    

def PRODUCTRECORDS(request):
    products= GymProducts.objects.all()

    context = {
        'products': products
    }
    
    return render(request,"admin/product.html",context)

@login_required(login_url="accounts/login/")
def cart_add(request, id):
    cart = Cart(request)
    product = get_object_or_404(GymProducts,id=id)
    cart.add(product)
    return redirect("cart_detail")


@login_required(login_url="accounts/login/")
def item_clear(request, id):
    cart = Cart(request)
    product = GymProducts.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="accounts/login/")
def item_increment(request, id):
    cart = Cart(request)
    product = GymProducts.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="accounts/login/")
def item_decrement(request, id):
    cart = Cart(request)
    product = GymProducts.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="accounts/login/")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="accounts/login/")
def cart_detail(request):
    
    return render(request, 'cart/cart.html')

def CHECKOUT(request):

    return render(request,"cart/checkout.html")

def POSTCHECKOUT(request):
     if request.method == 'POST':
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        country = request.POST.get('country')       
        address=request.POST.get('address')
        city = request.POST.get('city') 
        state = request.POST.get('state')
        postcode = request.POST.get('postcode')       
        email=request.POST.get('email')
        phone = request.POST.get('phone')  
        notes = request.POST.get('notes')
        amount = request.POST.get('amount')  
         
        print(first_name,last_name,email,country,address,city,state,postcode,email,phone)
        order = Order(
          firstname = first_name,
          lastname = last_name,
          country = country,
          address = address,
          city = city,
          state = state,
          postcode = postcode,
          email = email,
          phone = phone,
          additional_info = notes,
          amount = amount
        )
        print(order)
        order.save()
        return redirect('checkout')
        return render(request,"cart/checkout.html")

def ORDERS(request):
    order= Order.objects.all()

    context = {
        'order': order
    }
    return render(request,"admin/orderrecords.html",context)    