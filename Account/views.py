from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from .models import User
from Homepage.views import homepage

# Create your views here.
def account_signup(request):
    return render(request,'signup.html')


def retailer(request):
    return render(request, 'retailer.html')

def account_registration(request):
    if request.method == "POST":
       firstName = request.POST['first_name']
       lastName = request.POST['last_name']
       userEmail =request.POST['umail']
       retailer = request.POST['shopping_place']
       password = request.POST['user_password']
          
       content = User(User.first_name == firstName , User.last_name == lastName, User.user_email == userEmail 
                ,  User.retailer == retailer, User.password == password)
       content.save()
       print('Data was saved successfully')  
    return render(request,'signup.html')
        