from django.contrib import admin
from .models.menuitem import Menuitem
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order

# Register your models here.

class MenuitemsAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'description', 'image']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


# class CustomerAdmin(admin.ModelAdmin):
#     list_display = ['name', 'email', 'phone', 'username', 'password', 'confirmpass', 'wallet_balance']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['menuitem', 'customer', 'quantity', 'price', 'date']



admin.site.register(Menuitem, MenuitemsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Customer)
admin.site.register(Order, OrderAdmin)



