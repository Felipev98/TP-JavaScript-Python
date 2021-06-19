from django.urls import path
from . import views

urlpatterns = [
    path('',views.store, name="store"),
    path('car/',views.car, name="car"),
    path('checkout/',views.checkout, name="checkout"),

]