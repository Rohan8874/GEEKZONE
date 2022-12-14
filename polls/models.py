from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Customer(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    contact_address = models.CharField(max_length=200, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)


class Categories(models.Model):
    categories_id = models.IntegerField(primary_key=True)
    categories_name = models.CharField(max_length=125)
    categories_type = models.CharField(max_length=125)


class Delivery(models.Model):
    delivery_id = models.IntegerField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)


class Product(models.Model):
    products_id = models.IntegerField(primary_key=True)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)
    stock = models.IntegerField()
    name = models.CharField(max_length=100)
    price = models.FloatField()
    image = models.ImageField()
    star = models.IntegerField()


class Order(models.Model):
    order_id = models.IntegerField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.FloatField()
    date = models.IntegerField()


class Seller(models.Model):
    seller_id = models.IntegerField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=125)
    phone_number = models.IntegerField()
    photo = models.ImageField()
    email_address = models.EmailField()


class Payment(models.Model):
    payment_id = models.IntegerField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    payment_method = models.FloatField()
    amount = models.FloatField()


class Old_Product(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)
    name = models.CharField(max_length=125)
    image = models.ImageField()


class Review(models.Model):
    review_id = models.IntegerField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    comment = models.CharField(max_length=125)
    star = models.IntegerField()

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=100)
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Massage from ' + self.name + ' - ' + self.email
