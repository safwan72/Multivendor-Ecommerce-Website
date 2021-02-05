from django.urls import path
from . import views

app_name='App_Order'

urlpatterns = [
    path('add_toCart/<pk>/',views.add_to_cart,name='add_toCart'),
    path('viewCart/',views.cart_view,name='viewCart'),
    path('checkout/',views.checkout,name='checkout'),
    path('increase/<pk>/',views.increase,name='increase'),
    path('decrease/<pk>/',views.decrease,name='decrease'),
]
