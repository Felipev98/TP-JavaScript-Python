from django.urls import path
from . import views

urlpatterns = [
    path('',views.store, name="store"),
    path('car/',views.car, name="car"),
    path('checkout/',views.checkout, name="checkout"),
    path('update_Item',views.updateItem, name="update_Item"),


]