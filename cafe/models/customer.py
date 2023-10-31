import email
from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    phone = models.CharField(max_length = 15)
    username = models.CharField(max_length = 50)
    password = models.CharField(max_length = 100)
    confirmpass = models.CharField(max_length = 100)
    wallet_balance = models.FloatField(blank=True, null=True)

   # CREATING A METHOD TO SAVE THE CUSTOMER INFO INTO DATABASE.

    def register(self):
        self.save()

    def Emailexists(self):
        if Customer.objects.filter(email = self.email):
            return True
        else:
            return False

    
    def Idexists(self):
        if Customer.objects.filter(id = self.id):
            return True
        else:
            return False

    # def login_customer(self):
    #     if Customer.objects


    def UsernameExists(self):
        if Customer.objects.filter(username = self.username):
            return True
        else:
            return False


    @staticmethod
    def get_customer_by_email(loginemail):
        try:
            return Customer.objects.get(email = loginemail)
        except:
            return False




   
