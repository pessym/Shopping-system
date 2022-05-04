from django.db import models
from Account.models import Retailer, User

# Create your models here.


class Products(models.Model):
    product_name = models.CharField(max_length=255, null=True)
    image = models.CharField(max_length= 255, null=True,)
    category= models.CharField(max_length=150, unique=True,)
    actual_price = models.CharField(max_length=255, null=True, )
    offer_price = models.IntegerField(null= True)
    description = models.DateField(auto_now_add= True, null=True)
    retailer = models.ManyToManyField(Retailer)
    