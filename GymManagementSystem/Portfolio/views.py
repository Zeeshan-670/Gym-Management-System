from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def portfolio(request):
    #return HttpResponse("<h1>Portfolio</h1>")
    return render(request,'portfolio.html')
