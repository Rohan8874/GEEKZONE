from django . http import HttpResponse
from django.shortcuts import render


def home_page(request):
    return render(request, 'home.html')
def shop_page(request):
    return render(request, 'shop.html')
def about_page(request):
    return render(request, 'about.html')
def search_page(request):
    return render(request, 'search.html')
def cart_page(request):
    return render(request, 'cart.html')
def login_page(request):
    return render(request, 'login.html')
def categories(request):
    return render(request, 'categories.html')
def contact_page(request):
    return render(request, 'contact.html')
def dashboard_page(request):
    return render(request, 'dashboard.html')
def registration_page(request):
    return render(request, 'registration.html')
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
