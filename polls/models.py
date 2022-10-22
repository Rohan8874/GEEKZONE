from django.db import models


# Create your models here.

class Customer(models.Model):
    customer_id = models.IntegerField()
    user_id = models.IntegerField()
    contact_address = models.IntegerField()
    date = models.IntegerField()


class Order(models.Model):
    order_id = models.IntegerField()
    customer_id = models.IntegerField()
    product_id = models.IntegerField()
    amount = models.FloatField()
    date = models.IntegerField()


class Categories(models.Model):
    categories_id = models.IntegerField()
    categories_name = models.CharField(max_length=25)
    categories_type = models.CharField(max_length=25)


class Seller(models.Model):
    seller_id = models.IntegerField()
    order_id = models.IntegerField()
    user_id = models.IntegerField()
    name = models.CharField(max_length=25)
    phone_number = models.IntegerField()
    photo = models.ImageField()
    email_address = models.EmailField()


class Delivery(models.Model):
    delivery_id = models.IntegerField()
    customer_id = models.IntegerField()
    name = models.CharField(max_length=25)
    address = models.Varcher()


class Payment(models.Model):
    payment_id = models.IntegerField()
    order_id = models.IntegerField()
    customer_id = models.IntegerField()
    payment_method = models.FloatField()


class Product(models.Model):
    products_id = models.IntegerField()
    categories_id = models.IntegerField()
    stock = models.IntegerField()
    name = models.CharField(max_length=25)
    price = models.FloatField()
    image = models.ImageField()
    star = models.IntegerField()


class Transaction_Report(models.Model):
    report_id = models.IntegerField()
    payment_id = models.IntegerField()


class Old_Product(models.Model):
    product_id = models.IntegerField()
    seller_id = models.IntegerField()
    customer_id = models.IntegerField()
    categories_id = models.IntegerField()
    name = models.CharField(max_length=25)
    image = models.ImageField()


class Review(models.Model):
    review_id = models.IntegerField()
    product_id = models.IntegerField()
    customer_id = models.IntegerField()
    comment = models.CharField(max_length=25)
    star = models.IntegerField()

