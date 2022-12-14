from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import authenticate

from django.contrib import messages


from .models import *
from .forms import OrderForm, CreateUserFrom
#from .filters import Orderfilter
from polls.models import Contact
from django.contrib import messages
def home_page(request):
    return render(request, 'home2.html')
def about_page(request):
    messages.success(request, 'This is About')
    return render(request, 'about.html')
def search_page(request):
    return render(request, 'search.html')
def shop(request, products=None):
    products = products.objects.all()
    context = {'products': products}
    return render(request, 'shop.html', context)
def cart_page(request):
    return render(request, 'cart.html')
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')
    context = {}
    return render(request, 'login.html', context)
def logoutUser(request):
    logout(request)
    return redirect('login')
@login_required(login_url='login')
def categories(request):
    return render(request, 'categories.html')
def contact_page(request):
    messages.success(request, 'Welcome to contact')
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        print(name, email, phone, content)
        contact = Contact(name=name, email=email, phone=phone, content=content)
        contact.save()

    return render(request, 'contact.html')
def dashboard_page(request):
    return render(request, 'dashboard.html')
def registration_page(request):
        form = CreateUserFrom()

        if request.method == 'POST':
            form = CreateUserFrom(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        context = {'form': form}
        return render(request, 'registration.html', context)
@login_required(login_url='login')

def forget_password(request):
    return render(request, 'forget_password.html')
def order_page(request):
    return render(request, 'order.html')
def exchange_page(request):
    return render(request, 'exchange.html')
def save_payment_method(request):
    return render(request, 'payment.html')
def exchange_page(request):
    return render(request, 'exchange.html')
def account_page(request):
    return render(request, 'account.html')
def smartphone(request):
    return render(request, 'smart_phone.html')
def computer(request):
    return render(request, 'computer.html')
def accessories(request):
    return render(request, 'accessories.html')
def smart_watch(request):
    return render(request, 'smart_watch.html')

