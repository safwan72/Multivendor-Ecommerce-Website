from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
class SignUpForm(UserCreationForm):
    email=forms.CharField(required=True,label='Email',widget=forms.TextInput(attrs={'placeholder':"Enter Your Email",'class':'form-control','style':'margin-bottom:20px'}))
    username=forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder':"Enter Your Username",'class':'form-control','style':'margin-bottom:20px'}))
    password1=forms.CharField(required=True,label='Enter Your Password',widget=forms.PasswordInput(attrs={'placeholder':"Enter Your Password",'class':'form-control','style':'margin-bottom:20px'}))
    password2=forms.CharField(required=True,label='Confirm Your Password',widget=forms.PasswordInput(attrs={'placeholder':"Confirm Your Password",'class':'form-control','style':'margin-bottom:20px'}))
    class Meta:
        model=models.User
        fields=('email','username','password1','password2')
        
        
class CustomerProfile(UserChangeForm):
    class Meta:
        model=models.Customer
        exclude=('user',)
class SellerProfile(UserChangeForm):
    class Meta:
        model=models.Seller
        exclude=('user',)