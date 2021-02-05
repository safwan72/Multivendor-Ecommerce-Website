from django.db import models
from App_Login.models import Seller
# Create your models here.




        
class Product(models.Model):
    mainimage=models.ImageField(upload_to='products')
    name=models.CharField(max_length=264)
    added_by=models.ForeignKey(Seller,on_delete=models.CASCADE)
    preview_text=models.TextField(max_length=100,verbose_name='Preview Text')
    detail_text=models.TextField(max_length=1000,verbose_name='Detail Text')
    price=models.FloatField()
    old_price=models.FloatField(default=0.00)
    created_at=models.DateTimeField(auto_now_add=True)
    added_to_shop=models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering=['-created_at',]
        verbose_name_plural='Products'
        
        
        
class ShopOwner(models.Model):
    owner=models.ForeignKey(Seller,on_delete=models.CASCADE,related_name='shop_owner')
    shop_title=models.CharField(max_length=150,blank=True)
    products=models.ManyToManyField(Product)
    shop_created=models.BooleanField(default=False)
    shop_description=models.CharField(max_length=255,blank=True)
    shop_date=models.DateTimeField(auto_now_add=True,blank=True)
    def __str__(self):
        return self.shop_title
    
    class Meta:
        verbose_name_plural='Owner'