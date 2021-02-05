from django.urls import path
from . import views

app_name='App_Login'

urlpatterns = [
    path('',views.index,name='home'),
    path('customer_signup/',views.customer_signup_view,name='csignup'),
    path('seller_signup/',views.seller_signup_view,name='ssignup'),
    path('login/',views.login_view,name='login'),
    path('customer_update/',views.c_profilechange,name='customer_profile_update'),
    path('seller_update/',views.s_profilechange,name='seller_profile_update'),
    path('logout/',views.logout_view,name='logout'),
]
