from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.hashers import make_password, check_password
from django.views import View
from .models.customer import Customer
from cafe.models.menuitem import Menuitem


class Login_register(View):

    def get(self, request):
        return render(request, 'login_register.html')

    def post(self, request):

        data = {}
        if 'signup' in request.POST:
            # TAKING INPUTS FROM USER AND DISPLAYING IT.
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phoneno')
            username = request.POST.get('username')
            password = request.POST.get('password')
            confirmpass = request.POST.get('confirmpassword')
            wallet_balance = 0 #request.POST.get('walletbal')

            # PRINT THE INPUTS WE GOT FROM REGISTER PAGE
            print(name, email, phone, username,
                  password, confirmpass, wallet_balance)

            customer = Customer(
                name=name,
                email=email,
                phone=phone,
                username=username,
                password=password,
                confirmpass=confirmpass,
                wallet_balance=wallet_balance
            )

            # Validation
            error_message = None

            if request.POST.get('name') == "":
                error_message = "Please fill out your name !!"
            elif len(request.POST.get('name')) < 3:
                error_message = "Enter your full name !!"
            elif request.POST.get('email') == "":
                error_message = "Enter your email address !!"
            elif request.POST.get('phoneno') == "":
                error_message = "Phone number is required !!"
            elif len(request.POST.get('phoneno')) < 10:
                error_message = "Phone number should be 10 digits long !!"
            elif request.POST.get('username') == "":
                error_message = "Please create your username !!"
            elif request.POST.get('password') == "":
                error_message = "Password is required !!"
            elif len(request.POST.get('password')) < 6:
                error_message = "Password must be 6 characters long!"
            elif (request.POST.get('password')) != request.POST.get('confirmpassword'):
                error_message = "Password is not matching!!"
            elif customer.Emailexists():
                error_message = "Email is already registered!!"
            elif customer.UsernameExists():
                error_message = "Username is Taken."

            data = {
                'name': name,
                'phone': phone,
                'email': email,
                'username': username,
                'walletbalance': wallet_balance,
            }

            if not error_message:

                # Hashig the password befor saving it
                customer.password = make_password(customer.password)
                # Saving customer details into database
                customer.register()

                return redirect('index1')

            else:

                data = {
                    'name': name,
                    'phone': phone,
                    'email': email,
                    'username': username,
                    'walletbalance': wallet_balance,
                    'error': True,
                    'error_message': error_message
                }
                return render(request, 'login_register.html', data)



        elif 'login' in request.POST:

            loginemail = request.POST.get('loginemail')
            loginpassword = request.POST.get('loginpassword')
            print(loginemail, loginpassword)

            customer = Customer.get_customer_by_email(loginemail)

            error_message = None

            if customer:
                flag = check_password(loginpassword, customer.password)
                if flag:
                    request.session['customer_id'] = customer.id
                    request.session['email'] = customer.email
                    request.session['walletbal'] = customer.wallet_balance
                    return redirect ('index1')
                else:
                    error_message = "Invalid email or password!!"
                    # return render(request, 'login_register.html', data1)
            else:
                error_message = "Invalid email or password!!"

            data1 = {
                'error' : True,
                'error_message': error_message
            }
            return render(request, 'login_register.html', data1)

