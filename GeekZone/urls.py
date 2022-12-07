from django.urls import path, include
from django.contrib import admin
from polls import views as polls_views

#from django.conf import settings
#from django.conf.urls.static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', polls_views.home_page, name="home"),
    path('home/', polls_views.home_page, name="home"),
    path('shop/', polls_views.shop_page),
    path('about/', polls_views.about_page),
    path('search/', polls_views.search_page),
    path('cart/', polls_views.cart_page),
    path('login/', polls_views.login_page, name="login"),
    path('logout/', polls_views.logoutUser, name="logout"),
    path('categories/', polls_views.categories),
    path('contact/', polls_views.contact_page),
    path('dashboard/', polls_views.dashboard_page),
    path('registration/', polls_views.registration_page, name="register"),
    path('forget_password/', polls_views.forget_password),
    path('order/', polls_views.order_page),
    path('exchange/', polls_views.exchange_page),
    path('payment/', polls_views.save_payment_method),
    path('account/', polls_views.account_page),
    path('smartphone/', polls_views.smartphone),
    path('computer/', polls_views.computer),
    path('accessories/', polls_views.accessories),
    path('smart_watch/', polls_views.smart_watch),


]