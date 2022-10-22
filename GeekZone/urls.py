from django.contrib import admin
from django.urls import path, include
import polls.views as polls_views

#from django.conf import settings
#from django.conf.urls.static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', polls_views.home_page),
    path('home/', polls_views.home_page),
    path('shop/', polls_views.shop_page),
    path('about/', polls_views.about_page),
    path('search/', polls_views.search_page),
    path('cart/', polls_views.cart_page),
    path('login/', polls_views.login_page),
    path('categories/', polls_views.categories),
    path('contact/', polls_views.contact_page),
    path('dashboard/', polls_views.dashboard_page),
    path('registration/', polls_views.registration_page),
    path('forget_password/', polls_views.forget_password),
    path('order/', polls_views.order_page),
    path('exchange/', polls_views.exchange_page),
    path('payment/', polls_views.save_payment_method),
    path('account/', polls_views.account_page),


]