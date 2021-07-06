from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse
import json
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import permission_required

def store(request):
    category = Category.objects.all()
    if request.user.is_authenticated:
        customer = request.user.customer 
        order, created = Order.objects.get_or_create(customer=customer, complete=False )
        Items = order.orderitem_set.all()
        carItems = order.get_car_items
    else:
        Items = []
        order = {'get_car_total':0,'get_car_items':0 }
        carItems = order['get_car_items']

    products = Product.objects.order_by('-id')[:3]
    all_products= Product.objects.order_by('-id')[3:10]
    context = {'products':products, 'carItems': carItems, 'all_products':all_products,'category':category}
    return render(request,'store/store.html',context)

def category(request,cats):
    category = Category.objects.all()
    category_foods = Product.objects.filter(category=cats)
    return render(request, 'store/category.html',{'cats':cats,'category_foods':category_foods,'category':category})

def car(request):
    if request.user.is_authenticated:
        category = Category.objects.all()
        customer = request.user.customer 
        order, created = Order.objects.get_or_create(customer=customer, complete=False )
        Items = order.orderitem_set.all()
        carItems = order.get_car_items

    else:
        Items = []
        order = {'get_car_total':0,'get_car_items':0 }
        carItems = order.get_car_items
        carItems = order['get_car_items']

    context = {'Items': Items, 'order': order, 'carItems':carItems,'category':category }
    return render(request,'store/car.html',context)


def search(request):
    category = Category.objects.all()
    if request.method == "POST":
        searched = request.POST['searched']
        search = Product.objects.filter(name__contains=searched)
        return render(request,'store/search.html',{'searched':searched,'search':search,'category':category})
    else:
        return render(request,'store/search.html')
def acerca(request):
    category = Category.objects.all()
    context = {'category':category}
    return render(request,'store/acerca.html',context)
@permission_required('store.agregar')           
def agregar(request):
    data ={
        'form': ProductForm()
    }
    if request.method == 'POST':
        formulario = ProductForm(data= request.POST,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado correctamente"
        else:
             data["form"] = formulario   
    return render(request, 'CRUD/agregar.html',data)
@permission_required('store.modificar')           
def modificar(request,id):
    productoss = get_object_or_404(Product, id = id)
    data ={
        'form': ProductForm(instance=productoss)
    }

    if request.method == 'POST':
        formulario = ProductForm(data = request.POST,instance=productoss,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar")
        data["form"] = formulario
    return render(request,'CRUD/modificar.html',data)
@permission_required('store.eliminar')           
def eliminar(request,id):
    producto = get_object_or_404(Product,id=id)
    producto.delete()
    return redirect(to="listar")
@permission_required('store.listar')           
def listar(request):
    productosss = Product.objects.all()

    data ={
        'productos':productosss
    }
    return render(request,'CRUD/listar.html',data)

def product_details(request,id):
    if request.user.is_authenticated:
            customer = request.user.customer 
            order, created = Order.objects.get_or_create(customer=customer, complete=False )
            Items = order.orderitem_set.all()
            carItems = order.get_car_items
    else:
            Items = []
            order = {'get_car_total':0,'get_car_items':0 }
            carItems = order['get_car_items']
    product = Product.objects.get(id = id)

    return render(request,'store/mas.html',{'product':product,'carItems':carItems})

def registro(request):
    
    data ={
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request,user)
            return redirect(to="/")
        data["form"] = formulario     
    return render(request,'registration/registro.html',data)


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
    elif action == 'remove_all':
        orderItem.quantity = 0
    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe= False)

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
    elif action == 'remove_all':
        orderItem.quantity = 0
    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe= False)
def clearCar(request):
    data = json.loads(request.body)
    action = data['action']

    print('Action: ',action)

    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False )
    orderItem, created = OrderItem.objects.get_or_create(order = order)
    
    if action == 'remove_all':
        orderItem.quantity = 0
    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe= False)


