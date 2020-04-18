from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    category_name= models.CharField(max_length=200)
    def __unicode__(self):
        return u'%s' % self.category_name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    img_url = models.CharField(max_length=200, default=0)
    def __unicode__(self):
        return str(self.product_name, 'utf-8')

class State(models.Model):
    name = models.CharField(max_length=200)

class Order(models.Model):
    order_id = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    number = models.CharField(max_length=200)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    def __unicode__(self):
        return u'%s' % self.order_id



class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    def __unicode__(self):
        return str(self.product_name, 'utf-8')
