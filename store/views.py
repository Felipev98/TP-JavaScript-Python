from django.shortcuts import render
from .models import *

def store(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request,'store/store.html',context)

def car(request):
    context = {}
    return render(request,'store/car.html',context)

def checkout(request):
    context = {}
    return render(request,'store/checkout.html',context)
        