from django . http import HttpResponse
from django.contrib import admin
from django.shortcuts import render


def index(request):
    return render(request, "polls/index.html", {})

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