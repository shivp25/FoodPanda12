from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.hashers import make_password, check_password
from django.views import View
from .models.customer import Customer
from cafe.models.menuitem import Menuitem
from cafe.login_register import Login_register
from cafe.models.orders import Order

# Create your views here.


def Index(request):
    return render(request, 'index.html')


class Index1(View):
    def get(self, request):

        cart = request.session.get('cart')
        if not cart:
            request.session.cart = {}

        print('your id: ',request.session.get('customer_id'))
        print('you are: ', request.session.get('email'))
        print('your wallet balance: ', request.session.get('walletbal'))
        return render(request, 'index1.html')

    def post(self, request):

        cart = request.session.get('cart')
        if not cart:
            request.session.cart = {}

        if 'login_register' in request.POST:
            if 'signup' in request.POST:
                return render(request, 'menu.html')
            else:
                return redirect('loginregister')

        elif 'cart_icon' in request.POST:
            # elif request.POST.get('cart_icon'):
            return redirect( 'cartitems')

        # Logout
        elif 'logout_signout' in request.POST:
            request.session.clear()
            return redirect('loginregister')

        if 'signup' in request.POST:
            return redirect('menu')
        else:
            return render(request, 'index1.html')



def Menupage(request):
    return render(request, 'menupage.html')


class Menu(View):
    def get(self, request):

        cart = request.session.get('cart')
        if not cart:
            request.session.cart = {}

        menuitems = Menuitem.get_all_menuitems()
        data = {
            'menuitems': menuitems
        }
        # if request.method == "GET":
        #     return redirect('menu')
        # elif request.method == "POST":
        #     return redirect ("menu")
        return render(request, 'menu.html', data)

    def post(self, request):

        menuitem = request.POST.get('menuitem')
        remove = request.POST.get("remove")
        print(menuitem)

        cart = request.session.get('cart')

        if cart:
            quantity = cart.get(menuitem)

            if quantity:

                if remove:
                        if quantity<=1:
                            cart.pop(menuitem)
                        else:
                            cart[menuitem] = quantity - 1
                else:
                    cart[menuitem] = quantity + 1
                
            else:
                cart[menuitem] = 1
                
        else:
            cart = {}
            cart[menuitem] = 1

        request.session['cart'] = cart
        print(request.session['cart'])
        return redirect('menu')



class Wallet(View):
    
    def get(self, request):
        # existing_balance = request.session.get('walletbal')
        customer = Customer.objects.get(id = request.session.get('customer_id'))
        new_updated_wallet =  customer.wallet_balance 
        print("new_updated_wallet: " , new_updated_wallet)
        # request.session['walletbal'] = new_updated_wallet
        return render(request, 'wallet.html', {'new_updated_wallet': new_updated_wallet})

    def post(self, request):
        
        cid = request.session.get('customer_id')
        print("cid : ", cid)
        walletbal = request.POST.get('balance')
        
        if walletbal:
            print("walletbal: " , request.session.get('walletbal'))
            print("Adding walletbal: " , walletbal)
            updatedBal =  float(walletbal) + float(request.session.get('walletbal'))
            print("updated_walletbal : ", updatedBal)
            request.session['walletbal'] = updatedBal
            # if walletbal:
            #     updatedBal =float(walletbal) +float(updatedBal)

            # if request.session.get('customer_id'):
            #     cust = Customer.objects.get() 
            #     for a in cust:
            #         print("current name:" ,a.name)   

            if Customer.objects.get(id = request.session.get('customer_id')):
                cust = Customer.objects.get(id = request.session.get('customer_id')) 
                print(cust)
                print("Old wallet balance: ",  cust.wallet_balance)
                cust.wallet_balance = updatedBal
            # custo = Customer(
            #     wallet_balance=updatedBal
            # )
                cust.register()
            # new_updated_wallet =  cust.wallet_balance 
            # request.session['updated_walletbal'] = new_updated_wallet
                print("Updated wallet balance: ",  cust.wallet_balance)
                print("Current logged-in customer is:" , cust.id)
                print("Current logged-in customer name is:" , cust.name)
            # Customer.objects.filter(id = cid).update(cust.wallet_balance = updatedBal)
                # toupdate = Customer.objects.get(id = cid)
                # toupdate
            

            # cust.wallet_balance = updatedBal

        if not walletbal == "":
            again_updated = float(updatedBal) + float(walletbal)



        dataobj = {
            'walletbal': walletbal,
            'updated_balance': updatedBal,
            'again_updated': again_updated,
            'customer_id': cid,
            # 'new_updated_wallet': new_updated_wallet
        }

        # get id=(customer_id stored in session) record from customer table into Customer obj
        # e.g. Customer customer = all column data from database
        # then, update wallet balance with new value
        # e.g. customer.wallet_balance = updatedBal
        # then, store updated customer object in database and session

        # PRINT THE INPUTS WE GOT FROM REGISTER PAGE
        # print(name, email, phone, username,
        #         password, confirmpass, wallet_balance)

        return render(request, 'wallet.html', dataobj)


class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer_id')
        cart = request.session.get('cart')
        menuitems = Menuitem.get_menuitems_by_id(list(cart.keys()))
        print(address, phone, customer, cart, menuitems)

        for menuitem in menuitems:
            print(cart.get(str(menuitem.id)))
            order = Order(customer = Customer(id = customer),
                          menuitem = menuitem,
                          price = menuitem.price,
                          quantity = cart.get(str(menuitem.id)),
                          address = address,
                          phone = phone)
            
            print(order.placeOrder())

        request.session['cart'] = {}

        return redirect('cartitems')
    

class OrderView(View):
    def get(self, request):
        customer = request.session.get('customer_id')
        orders = Order.get_orders_by_customers(customer)
        print(orders)
        orders = orders.reverse()

        return render(request, 'orders.html', {'orders': orders})






