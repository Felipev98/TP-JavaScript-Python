from django.shortcuts import render
from .models import *
from django.http import JsonResponse

def store(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request,'store/store.html',context)

def car(request):
    if request.user.is_authenticated:
        customer = request.user.customer 
        order, created = Order.objects.get_or_create(customer=customer, complete=False )
        Items = order.orderitem_set.all()
    else:
        Items = []
        order = {'get_car_total':0,'get_car_items':0 }
    context = {'Items': Items, 'order': order}
    return render(request,'store/car.html',context)

def checkout(request):
    context = {}
    return render(request,'store/checkout.html',context)

def updateItem(request):
    return JsonResponse('Item was added', safe= False)
