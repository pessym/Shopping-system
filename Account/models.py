
from django.db import models

# Create your models here.
class Retailer(models.Model):
    location  = (
        ('Busia','Busia' ),
        ('Kisumu', 'Kisumu'),
        ('Nairobi', 'Nairobi'),
        ('Kisii', 'Kisii'),
        ('Nakuru', 'Nakuru',)
    )      
    retailer_name = models.CharField(max_length=255, null=True)
    retailer_email = models.CharField(max_length=150, unique=True,)
    location = models.CharField(max_length=255, null=True, choices=location)
    password = models.CharField(max_length=255, null=True, )    
    date_created = models.DateField(auto_now_add= True, null=True)


class User(models.Model):
    first_name = models.CharField(max_length=255, null=True,)
    last_name = models.CharField(max_length=255, null=True,)
    user_email = models.CharField(max_length=150, unique=True,)
    password = models.CharField(max_length=255, null=True, )
    retailer = models.ForeignKey(Retailer, on_delete = models.CASCADE)
    date_created = models.DateField(auto_now_add= True, null=True)
    

