from django.urls import path
from .views import account_registration, retailer


urlpatterns = [
    #path('signup', account_signup , name='account_signup' ),
    path('signup/', account_registration , name='account_registration' ),
    path('retailer/', retailer , name='retailer-page' ),
    
]