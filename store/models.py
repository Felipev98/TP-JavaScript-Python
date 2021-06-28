from django.db import models
from django.contrib.auth.models import User



class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name
class Category(models.Model):
    category =models.CharField(max_length=255,default="Comidas")

    def __str__(self):
        return self.category
class Product(models.Model):
    name= models.CharField(max_length=200,null = True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    img = models.ImageField(null= True,blank=True)
    description = models.CharField(max_length=255,default="")
    category = models.CharField(max_length=255,default="Comidas")
    def __str__(self):
        return self.name
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete = models.SET_NULL,blank=True,null=True)
    date_orderd = models.DateTimeField(auto_now_add= True)
    complete = models.BooleanField(default= False, null= True, blank= False)
    transaction_id = models.CharField(max_length=200,null=True)
    def __str__(self):
        return str(self.id)

    @property
    def get_car_total(self):
        orderitems = self.orderitem_set.all()
        total =sum([Item.get_total for Item in orderitems])
        return total
    
    @property
    def get_car_items(self):
        orderitems = self.orderitem_set.all()
        total =sum([Item.quantity for Item in orderitems])
        return total           
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete = models.SET_NULL,blank=True,null=True)
    order = models.ForeignKey(Order, on_delete = models.SET_NULL,blank=True,null=True)
    quantity = models.IntegerField(default=0,null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add = True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total  



