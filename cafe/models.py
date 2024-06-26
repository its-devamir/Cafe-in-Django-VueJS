from django.db import models

class User(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    phone_number = models.IntegerField()

class Product(models.Model):
    name = models.CharField(max_length=255)
    sugar = models.IntegerField()
    coffee = models.IntegerField()
    flour = models.IntegerField()
    chocolate = models.IntegerField()
    category = models.CharField(max_length=255)
    price = models.IntegerField()
    image = models.ImageField(upload_to='products/')

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    products = models.ManyToManyField(Product, through='OrderProduct')
    purchase_amount = models.IntegerField()
    type = models.BinaryField(max_length=1)

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class Admin(models.Model):
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

class Storage(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
