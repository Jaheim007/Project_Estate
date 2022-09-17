from django.shortcuts import render
from django.views.generic import View

from Authentication import models


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