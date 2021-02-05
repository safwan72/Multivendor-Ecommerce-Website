from django.urls import path
from . import views

app_name='App_Shop'

urlpatterns = [
    path('',views.createshop,name='shop_create'),
    path('add_product/',views.addproduct,name='add_product'),
    path('allproducts/',views.viewproducts,name='allproducts'),
    path('addtoshop/<pk>/',views.addtoshop,name='addtoshop'),
    path('viewproduct/<pk>/',views.ProductDetail.as_view(),name='viewproduct'),
]
