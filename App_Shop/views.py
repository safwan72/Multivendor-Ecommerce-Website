from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404,render,HttpResponseRedirect
from django.urls import  reverse,reverse_lazy
from . import forms,models
from django.contrib.auth.decorators import login_required
from App_Login.models import Seller
from App_Login.decorators import seller
from django.views.generic import ListView,DetailView

from django.contrib.auth.mixins import LoginRequiredMixin

class ProductDetail(DetailView,LoginRequiredMixin):
    model=models.Product
    template_name='App_Shop/productdetail.html'
    context_object_name='product'    
    

# Create your views here.
@login_required
@seller()
def createshop(request):
    user=get_object_or_404(Seller,user=request.user)
    shop=models.ShopOwner.objects.filter(owner=user)
    if shop.exists():
        shop=shop[0]
    form=forms.ShopCreator()
    if request.method=='POST':
        form=forms.ShopCreator(request.POST) 
        if form.is_valid():
            shopform=form.save(commit=False)
            shopform.owner=user
            shopform.shop_created=True
            shopform.save()
            messages.success(request, 'Shop Created Succesfully')
            return HttpResponseRedirect(reverse('App_Shop:shop_create'))
    return render(request,'App_Shop/shop.html',context={'form':form,'shop':shop})


@login_required
@seller()
def addproduct(request):
    user=get_object_or_404(Seller,user=request.user)
    form=forms.AddProducts()
    if request.method=='POST':
        form=forms.AddProducts(request.POST,request.FILES) 
        if form.is_valid():
            productform=form.save(commit=False)
            if 'mainimage'in request.FILES:          #Applies for all kind of files pdf,doc,etc. 
                productform.mainimage=request.FILES['mainimage']
            productform.added_by=user
            productform.save()
            messages.success(request, 'Product Added Succesfully')
            return HttpResponseRedirect(reverse('App_Login:home'))
    return render(request,'App_Shop/productadd.html',context={'form':form})


@login_required
@seller()
def viewproducts(request):
    user=get_object_or_404(Seller,user=request.user)
    shop=models.ShopOwner.objects.get(owner=user,shop_created=True)
    shop_products=shop.products.all()
    user_products=models.Product.objects.filter(added_by=user,added_to_shop=False)
    return render(request,'App_Shop/products.html',context={'shop':shop,'user_products':user_products,'shop_products':shop_products})
    
    
@login_required
@seller()
def addtoshop(request,pk):
    user=get_object_or_404(Seller,user=request.user)
    shop=models.ShopOwner.objects.get(owner=user,shop_created=True)
    user_products=models.Product.objects.filter(added_by=user,pk=pk,added_to_shop=False)
    if user_products.exists():
        user_products=user_products[0]
    shop.products.add(user_products)
    user_products.added_to_shop=True
    user_products.save()
    shop.save()
    messages.success(request, 'Added to Shop Succesfully')
    return HttpResponseRedirect(reverse('App_Login:home'))


