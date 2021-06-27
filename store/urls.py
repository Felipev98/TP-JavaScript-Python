from django.urls import path
from . import views

urlpatterns = [
    path('',views.store, name="store"),
    path('acerca/',views.acerca, name="acerca"),
    path('contacto/',views.contacto, name="contacto"),
    path('car/',views.car, name="car"),
    path('checkout/',views.checkout, name="checkout"),
    path('update_item/',views.updateItem, name="update_item"),
    path('agregar/',views.agregar, name="agregar"),
    path('modificar/<id>/',views.modificar, name="modificar"),
    path('eliminar/<id>/',views.eliminar, name="eliminar"),
    path('listar/',views.listar, name="listar"),
    path('registro/',views.registro, name="registro")




]