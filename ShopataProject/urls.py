from Products import views
from django.contrib import admin
from django.urls import path, include
from Homepage import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("Homepage.urls")),
    path('', include("Account.urls")),
]
