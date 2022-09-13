from django.shortcuts import render , redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import login, authenticate, logout

from Authentication import models
from Authentication.forms import NewUserForm , LoginForm , UpdateProfile , AddProperty

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

def loginform(request):
    form = LoginForm(request.POST)
    if form.is_valid():     
        user = authenticate(
            username=form.cleaned_data["username"], 
            password=form.cleaned_data["password"]
        )
        
        if user:
            login(request, user)
            return redirect("/") 
        else:     
            print("User not Found") 
    return render(request , "pages/login.html" , locals())

def register(request):
    form = NewUserForm
    if request.method == 'POST':
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        user_type = request.POST.get("user_type")
        
        
        user = get_user_model().objects.create_user(
                first_name = first_name,
                last_name = last_name,
                username = username, 
                email = email, 
                password = password1, 
                user_type = user_type 
        )
        
        user.save()
            
        return redirect("/login")
    return render(request , "pages/register.html" , locals())

def logout_form(request):
    logout(request)
    return redirect("/")

def profile(request):

    return render(request ,  "pages/profile.html" , locals())

def edit_profile(request):
    
    form = UpdateProfile(instance=request.user)
   
    
    return render(request ,  "pages/edit_profile.html" , locals())
    


def about(request):
    return render(request , 'pages/about.html' , locals())

def add_property(request):
    
    form = AddProperty
 
    
    return render(request , 'pages/add_property.html' , locals())
    







# Create your views here.
