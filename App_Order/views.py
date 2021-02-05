from django.shortcuts import render, get_object_or_404, redirect


from django.contrib.auth.decorators import login_required

from django.contrib import messages

from . import models
from App_Shop.models import Product
from App_Login.models import Customer
from App_Login.decorators import customer

# Create your views here.
@login_required
@customer()
def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    customer = get_object_or_404(Customer, user=request.user)
    print(product)
    cart = models.Cart.objects.get_or_create(
        product=product, user=customer, purchased=False)
    print(cart)
    order = models.Order.objects.filter(user=customer, ordered=False)
    if order.exists():
        order = order[0]

        if order.cart_items.filter(product=product).exists():
            cart[0].quantity += 1
            cart[0].save()
            messages.success(request, 'Cart Updated Succesfully')
        else:
            order.cart_items.add(cart[0])
            order.save()
            messages.success(request, 'Item Added to Cart Succesfully')
    else:
        order = models.Order(user=customer)
        order.save()
        order.cart_items.add(cart[0])
        order.save()
        messages.success(
            request, 'Cart was Created Succesfully and Item Added')
    return  redirect("App_Order:viewCart")

@login_required
@customer()
def cart_view(request):
    customer = get_object_or_404(Customer, user=request.user)
    carts = models.Cart.objects.filter(user=customer, purchased=False)
    orders = models.Order.objects.filter(user=customer, ordered=False)
    if carts.exists() and orders.exists():
        order = orders[0]
        return render(request, 'App_Order/Cart.html', context={'order': order,'cart':carts})
    else:
        messages.warning(request, "You Dont Have Any Items in The Cart")
        return redirect("App_Login:home")
    

@login_required
@customer()
def increase(request,pk):
    customer = get_object_or_404(Customer, user=request.user)
    product = get_object_or_404(Product, pk=pk)
    # carts = models.Cart.objects.filter(user=customer, purchased=False)
    orders = models.Order.objects.filter(user=customer, ordered=False)
    if orders.exists():
        order=orders[0]
        if order.cart_items.filter(product=product).exists():
            cart=models.Cart.objects.filter(product=product,user=customer,purchased=False)
            cart=cart[0]
            if cart.quantity>=1:
                cart.quantity+=1
                cart.save()
                messages.success(request,'Item Increased Succesfully')
            else:
                messages.warning(request, "You Dont Have this item in The Cart")
                return redirect("App_Login:home")

    return  redirect("App_Order:viewCart")


@login_required
@customer()
def decrease(request,pk):
    customer = get_object_or_404(Customer, user=request.user)
    product = get_object_or_404(Product, pk=pk)
    # carts = models.Cart.objects.filter(user=customer, purchased=False)
    orders = models.Order.objects.filter(user=customer, ordered=False)
    if orders.exists():
        order=orders[0]
        if order.cart_items.filter(product=product).exists():
            cart=models.Cart.objects.filter(product=product,user=customer,purchased=False)
            cart=cart[0]
            if cart.quantity>1:
                cart.quantity-=1
                cart.save()
                messages.warning(request, "Quantity Decreased...")
            else:
                order.cart_items.remove(cart)
                cart.delete()
                messages.warning(request, "You Dont Have this item in The Cart")
                return redirect("App_Login:home")

    return  redirect("App_Order:viewCart")


@login_required
@customer()
def checkout(request):
    customer = get_object_or_404(Customer, user=request.user)
    orders = models.Order.objects.filter(user=customer, ordered=False)
    if orders.exists():
        order=orders[0]
        cart=models.Cart.objects.filter(user=customer,purchased=False)[0]
        order.ordered=True
        cart.purchased=True
        order.save()
        cart.save()
        messages.success(request, "Checkout Successfull")
    else:
        messages.warning(request, "Add Someitems to checkout")
        return redirect("App_Login:home")
    
    return redirect("App_Login:home")