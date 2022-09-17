from django.contrib.auth import get_user_model
from django.shortcuts import render , redirect
from django.views.generic import View
from django.contrib.auth import login, authenticate, logout

from Authentication import models
from Authentication import forms 


class Login(View):
    template_name = 'pages/login.html'
    class_form = forms.LoginForm
    
    def get(self , request):
        form = self.class_form
        return render(request , self.template_name , locals())
    
    def post(self , request):
        form = self.class_form(request.POST)
        if form.is_valid():     
            user = authenticate(
                username=form.cleaned_data["username"], 
                password=form.cleaned_data["password"]
            )
        if user:
            login(request, user)
            return redirect("/") 
        
        return render(request , "pages/login.html" , locals())
        
class Register(View):
    template_name = "pages/register.html"
    class_form = forms.NewUserForm
    
    def get(self , request):
        form = self.class_form
        return render(request , self.template_name , locals())
    
    def post(self , request):
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
        
class Logout(View):
    
    def get(self , request):
       logout(request)
       return redirect("/") 

class Profile(View):
    template_name = 'pages/profile.html'
    
    def get(self , request):
        return render(request , self.template_name , locals())
    
    def post(self , request):
        pass
    
class Edit_Profile(View):
    template_name = 'pages/edit_profile.html'
    
    def get(self, request):
        form = forms.UpdateProfile(instance=request.user)
        return render(request , self.template_name , locals())
    
    def post(self , request):
        pass
    
    
