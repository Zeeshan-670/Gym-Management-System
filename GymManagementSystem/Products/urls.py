from django.contrib import admin
from django.urls import path,include
from . import views



urlpatterns = [
    path('products/',view=views.Products,name="products"),


    #Admin Panel
    path('productrecords',view=views.PRODUCTRECORDS,name="productrecords"),
    path('addproducts/',view=views.ADDPRODUCTS,name="addproducts"),
    path('postaddproduct/',view=views.POSTADDPRODUCT,name="postAddProduct"),
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
    path('cart/checkout/',view=views.CHECKOUT,name="checkout"),
    path('cart/checkout/post',view=views.POSTCHECKOUT,name="checkoutpost"),


    path('orderrecords/',view=views.ORDERS,name="orders")
]
