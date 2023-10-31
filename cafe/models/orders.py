from django.db import models
from .customer import Customer
from .category import Category
from .menuitem import Menuitem
import datetime

class Order(models.Model):
    menuitem = models.ForeignKey(Menuitem, on_delete = models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    quantity = models.IntegerField(default = 1)
    price = models.IntegerField()
    address = models.CharField(max_length = 100, default = '', blank = True)
    phone = models.CharField(max_length = 15, default = '', blank = True)
    date = models.DateField(default = datetime.datetime.today)
    status = models.BooleanField(default = False)

    def placeOrder(self):
        self.save()


    @staticmethod
    def get_orders_by_customers(customer_id):
        return Order.objects.filter(customer = customer_id)