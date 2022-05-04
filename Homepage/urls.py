from Products import views
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage),
    path('', include("Account.urls")),
]
