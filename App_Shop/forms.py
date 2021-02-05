from . import models
from django import forms

class ShopCreator(forms.ModelForm):
    class Meta:
        model=models.ShopOwner
        fields=('shop_title','shop_description',)
    
class AddProducts(forms.ModelForm):
    class Meta:
        model=models.Product
        exclude=('added_by','added_to_shop',)