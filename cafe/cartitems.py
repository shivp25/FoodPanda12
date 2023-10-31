from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.hashers import make_password, check_password
from django.views import View
from .models.customer import Customer
from cafe.models.menuitem import Menuitem


class Cart(View):

    def get(self, request):
        
        ids = list(request.session.get('cart').keys())
        print(ids)
        menuitems = Menuitem.get_menuitems_by_id(ids)
        print(menuitems)
        return render (request, "cart.html", {'menuitems': menuitems})
        

    
        