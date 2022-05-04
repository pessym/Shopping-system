from django.contrib import admin

from Account.models import Retailer, User

# Register your models here.

admin.site.register(User)
admin.site.register(Retailer)