from django.db import models
from App_Login.models import Customer
from App_Shop.models import Product

# Create your models here.
class Cart(models.Model):
    user=models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='customer')
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    added_time=models.DateTimeField(auto_now_add=True)
    purchased=models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.product} X {self.quantity}'
    
    def get_total(self):
        return float(self.product.price*self.quantity)
    
    
    
class Order(models.Model):
    user=models.ForeignKey(Customer,on_delete=models.CASCADE)
    cart_items=models.ManyToManyField(Cart)
    added_at=models.DateTimeField(auto_now_add=True)
    ordered=models.BooleanField(default=False)
    couponcode=models.CharField(max_length=100,blank=True)
    
    def get_total_price(self):
        total=0
        for i in self.cart_items.all():
           total+=float(i.get_total())
        return total 
    
    
    