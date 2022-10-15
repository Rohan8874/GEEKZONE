from django.urls import path
from django.contrib import admin

from django . http import HttpResponse
from . import views

def home(request):
    return HttpResponse("Welcome to Home Page")
def shop(request):
    return HttpResponse("Welcome to Shop Page")
def about(request):
    return HttpResponse("Describe our website")
def search(request):
    return HttpResponse("Welcome to Search Page")
def cart(request):
    return HttpResponse("Welcome to Cart Page")
def login(request):
    return HttpResponse("login and registration page")
def categories(request):
    return HttpResponse("Show all categories")
def contact(request):
    return HttpResponse("Show our phone number")
def dashboard(request):
    return HttpResponse("Show some importance part")
def registration(request):
    return HttpResponse("when you have not to a account our website")
def forget_password(request):
    return HttpResponse("when you forget your password")
def order(request):
    return HttpResponse("customer order list")
def exchange(request):
    return HttpResponse("customer exchange his product")
def payment(request):
    return HttpResponse("save payment method")
def Account(request):
    return HttpResponse("Account details")
def settings(request):
    return HttpResponse("settings")
def smartphone(request):
    return HttpResponse("smartphone")
def computer(request):
    return HttpResponse("computer")
def accessories(request):
    return HttpResponse("accessories")
def smart_watch(request):
    return HttpResponse("smart_watch")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('', home),
    path('shop/', shop),
    path('about/', about),
    path('search/', search),
    path('cart/', cart),
    path('login/', login),
    path('contact/', contact),
    path('dashboard/', dashboard),
    path('registration/', registration),
    path('forget_password/', forget_password),
    path('my_order/', order),
    path('2nd_hand_product_buy_and_sell/', exchange),
    path('save_payment_method/', payment),
    path('Account_information/', Account),
    path('settings/', settings),
    path('smartphone/', smartphone),
    path('computer/', computer),
    path('accessories/', accessories),
    path('smart_watch/', smart_watch),



 ]