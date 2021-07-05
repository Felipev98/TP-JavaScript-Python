from django.urls import path
from . import views

urlpatterns = [
    path('',views.store, name="store"),
    path('acerca/',views.acerca, name="acerca"),
    path('car/',views.car, name="car"),
    path('update_item/',views.updateItem, name="update_item"),
    path('agregar/',views.agregar, name="agregar"),
    path('modificar/<id>/',views.modificar, name="modificar"),
    path('eliminar/<id>/',views.eliminar, name="eliminar"),
    path('listar/',views.listar, name="listar"),
    path('registro/',views.registro, name="registro"),
    path('category/<str:cats>/',views.category, name='category'),
    path('search/',views.search, name='search'),
    path('product_details/<int:id>',views.product_details, name='product_details'),


]