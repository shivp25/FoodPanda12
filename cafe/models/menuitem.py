from django.db import models
from .category import Category


# Creating model Menuitems where we can add our menu items from admin side.

class Menuitem(models.Model):
    name = models.CharField(max_length = 100)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete = models.CASCADE, blank=True, null=True)
    description = models.CharField(max_length = 300, default='', blank=True, null=True)
    image = models.ImageField(upload_to = 'uploads/menuitems/')

    @staticmethod
    def get_all_menuitems():
        return Menuitem.objects.all()

    
    @staticmethod
    def get_menuitems_by_id(ids):
        return Menuitem.objects.filter(id__in = ids)