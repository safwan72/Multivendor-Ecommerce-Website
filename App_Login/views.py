from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.urls import reverse, reverse_lazy
from . import forms, models
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from App_Login.decorators import customer,seller
from App_Shop.models import ShopOwner,Product



# Create your views here.


def index(request):
    product=Product.objects.filter(added_to_shop=True)
    return render(request, 'Home.html', context={'product':product})


def seller_signup_view(request):
    form = forms.SignUpForm()
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_customer = False
            user.is_seller = True
            user.save()
            seller = models.Seller(user=user)
            seller.save()
            messages.success(request, 'Account Created Successfully')
            return HttpResponseRedirect(reverse('App_Login:home'))
    return render(request, 'App_Login/Signup.html', context={'form': form, 'message': 'Sign Up As A Seller', 'btnval': 'SignUp'})


def customer_signup_view(request):
    form = forms.SignUpForm()
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_customer = True
            user.is_seller = False
            user.save()
            cust = models.Customer(user=user)
            cust.save()
            messages.success(request, 'Account Created Successfully')
            return HttpResponseRedirect(reverse('App_Login:home'))
    return render(request, 'App_Login/Signup.html', context={'form': form, 'message': 'Sign Up As A Customer', 'btnval': 'SignUp'})


def login_view(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('App_Login:home'))
            messages.success(request, 'Logged in Successfully')
        else:
            messages.warning(request, 'Log In Failed. Check Proper Inputs')
            return HttpResponseRedirect(reverse('App_Login:login'))
    return render(request, 'App_Login/Login.html', context={'message': 'Login Page', 'form': form, 'btnval': 'Login'})

@login_required
@customer()
def c_profilechange(request):
    user=request.user
    customer=models.Customer.objects.get(user=user)
    form=forms.CustomerProfile(instance=customer)
    if request.method=='POST':
        form=forms.CustomerProfile(request.POST,instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile Update Succesfully')
            return HttpResponseRedirect(reverse('App_Login:customer_profile_update'))
        else:
            messages.warning(request, 'Error Updating Profile.Try Again')
            return HttpResponseRedirect(reverse('App_Login:customer_profile_update'))
    return render(request,'App_Login/ProfileChange.html',context={'message': 'Profile Update', 'form': form, 'btnval': 'Update'})

@login_required
@seller()
def s_profilechange(request):
    user=request.user
    seller=models.Seller.objects.get(user=user)
    form=forms.SellerProfile(instance=seller)
    if request.method=='POST':
        form=forms.SellerProfile(request.POST,instance=seller)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile Update Succesfully')
            return HttpResponseRedirect(reverse('App_Login:seller_profile_update'))
        else:
            messages.warning(request, 'Error Updating Profile.Try Again')
            return HttpResponseRedirect(reverse('App_Login:seller_profile_update'))
    return render(request,'App_Login/ProfileChange.html',context={'message': 'Profile Update', 'form': form, 'btnval': 'Update'})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('App_Login:home'))
