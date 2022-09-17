from django.shortcuts import render , redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import login, authenticate, logout

from Authentication.forms import NewUserForm , LoginForm , UpdateProfile , AddProperty
from Property.models import Properties

def home(request):
    return render(request, "pages/index.html" , locals())

def property(request):
    return render(request , "pages/property.html" , locals())

def contact(request):
    return render(request , "pages/contact.html" , locals())

def about(request):
    return render(request , "pages/about.html" , locals())

def element(request):
    return render(request , "pages/elements.html" , locals())

    
    
def about(request):
    return render(request , 'pages/about.html' , locals())



def add_property(request):
    form = AddProperty
    if request.method =='POST':
        name = request.POST.get("name")
        price = request.POST.get("price")
        users = request.user
        
        print(request.user)
         
        property = Properties(
            name = name, 
            price = price,
            users = users
        )
        
        property.save()
    
    return render(request , "pages/add_property.html" , locals())

# def submit_property(request):    
#     return render(request, 'pages/add_property.html', locals())









# Create your views here.
