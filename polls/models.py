from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Customer(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    contact_address = models.IntegerField()
    date = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Categories(models.Model):
    categories_id = models.IntegerField(primary_key=True)
    categories_name = models.CharField(max_length=25)
    categories_type = models.CharField(max_length=25)


class Delivery(models.Model):
    delivery_id = models.IntegerField(primary_key=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    address = models.CharField(max_length=25)


class Product(models.Model):
    products_id = models.IntegerField(primary_key=True)
    categories_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
    stock = models.IntegerField()
    name = models.CharField(max_length=25)
    price = models.FloatField()
    image = models.ImageField()
    star = models.IntegerField()


class Order(models.Model):
    order_id = models.IntegerField(primary_key=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.FloatField()
    date = models.IntegerField()


class Seller(models.Model):
    seller_id = models.IntegerField(primary_key=True)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    phone_number = models.IntegerField()
    photo = models.ImageField()
    email_address = models.EmailField()


class Payment(models.Model):
    payment_id = models.IntegerField(primary_key=True)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    payment_method = models.FloatField()


class Transaction_Report(models.Model):
    report_id = models.IntegerField(primary_key=True)
    payment_id = models.ForeignKey(Payment, on_delete=models.CASCADE)


class Old_Product(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    seller_id = models.ForeignKey(Seller, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    categories_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    image = models.ImageField()


class Review(models.Model):
    review_id = models.IntegerField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    comment = models.CharField(max_length=25)
    star = models.IntegerField()
