"""spiceandherbs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cafe import views
from cafe import login_register
from cafe import cartitems

urlpatterns = [

    path('', views.Index, name='index'),
    path('index1/', views.Index1.as_view(), name='index1'),
    path('menu/', views.Menu.as_view(), name='menu'),
    path('menupage/', views.Menupage, name='menupage'),
    path('login-registration/', login_register.Login_register.as_view(), name='loginregister'),
    path('cart/', cartitems.Cart.as_view(), name='cartitems'),
    path('wallet/', views.Wallet.as_view(), name='wallet'),
    path('check-out', views.CheckOut.as_view() , name='checkout'),
    path('orders', views.OrderView.as_view(), name='order')
]
