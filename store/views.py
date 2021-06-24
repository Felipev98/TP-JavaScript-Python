from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import *

def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer 
        order, created = Order.objects.get_or_create(customer=customer, complete=False )
        Items = order.orderitem_set.all()
        carItems = order.get_car_items
    else:
        Items = []
        order = {'get_car_total':0,'get_car_items':0 }
        carItems = order['get_car_items']

    products = Product.objects.all()
    context = {'products':products, 'carItems': carItems}
    return render(request,'store/store.html',context)

def category(request):
    return {
        'category': Category.objects.all()
    }

def car(request):
    if request.user.is_authenticated:
        customer = request.user.customer 
        order, created = Order.objects.get_or_create(customer=customer, complete=False )
        Items = order.orderitem_set.all()
        carItems = order.get_car_items

    else:
        Items = []
        order = {'get_car_total':0,'get_car_items':0 }
        carItems = order.get_car_items
        carItems = order['get_car_items']

    context = {'Items': Items, 'order': order, 'carItems':carItems }
    return render(request,'store/car.html',context)

def checkout(request):
    context = {}
    return render(request,'store/checkout.html',context)
def contacto(request):
    context = {}
    return render(request,'store/contacto.html',context)
def acerca(request):
    context = {}
    return render(request,'store/acerca.html',context)        

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action: ',action)
    print('productId: ', productId)

    customer = request.user.customer
    product = Product.objects.get(id =productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False )
    orderItem, created = OrderItem.objects.get_or_create(order = order, product = product)
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1 )
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1 )
    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe= False)

