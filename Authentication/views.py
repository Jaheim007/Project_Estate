from django.contrib.auth import get_user_model
from django.shortcuts import render , redirect
from django.views.generic import View
from django.contrib.auth import login, authenticate, logout
from django.core.mail import send_mail
from django.contrib.auth.forms import SetPasswordForm , PasswordResetForm


from Authentication import models
from Authentication import forms 
from Property import models


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
            return redirect("myproperty") 
        
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

        send_mail(
                "Konato Account",
                "Your seller's account was created with success. ",
                'jaheimkouaho@gmail.com',
                [email],
                fail_silently=False
        )

        return redirect("/login")
 
    


    
        
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
    class_form = forms.EditProfile
    
    def get(self, request):
        form = self.class_form(instance=request.user)
        return render(request , self.template_name , locals())
    
    def post(self , request):
        form = self.class_form(request.POST, request.FILES, instance=request.user)
        print(request.POST)
        print(request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect("edit_profile")
        return redirect("profile")
    
    
class AddProperty(View):
    template_name = 'pages/add_property.html'
    add_form = forms.AddProperty
    
    def get(self , request):
        form = self.add_form
        return render(request , self.template_name , locals())
    
    def post(self , request):
        msg =''
        success = True
        
        name = request.POST.get("name")
        price = request.POST.get("price")
        status = request.POST.get('status')
        address_name = request.POST.get('address_name')
        property_type = request.POST.get('property_type')
        description = request.POST.get('description')
        bedroom = request.POST.get("bedroom")
        bathroom = request.POST.get("bathroom")
        garage = request.POST.get("garage")
        main_image = request.POST.get("main_image")
        users = request.user
        
        instance_bedroom = models.Bedrooms.objects.get(pk=bedroom)
        instance_bathroom = models.Bathrooms.objects.get(pk=bathroom)
        instance_garage = models.Garages.objects.get(pk=garage)
        instance_type_property = models.TypeProperty.objects.get(pk=property_type)
            
         
        property = models.Properties(
            name = name, 
            price = price,
            status = status,
            address_name = address_name,
            property_type = instance_type_property,
            description = description , 
            bedroom = instance_bedroom, 
            bathroom = instance_bathroom, 
            garage = instance_garage, 
            main_image = main_image,
            users = users
        )
        
        property.save()
        
        msg = 'Your email has been saved, we will keep you updated on our latest info.'
        
        data = {
        'msg': msg,
        'success': success
        }
        
        return redirect("myproperty")
      
class PasswordChange(View):
    template_name = 'pages/password_change.html'
    
    def get(self , request):
        user = request.user
        form = forms.ChangePassword(user)
        return render(request , self.template_name , locals())
    
    def post(self , request):
        user = request.user
        form = SetPasswordForm(user, request.POST)
        if form.is_valid():
            form.save()
            print('password changed')
            return redirect('login')
        else:
            for error in list(form.errors.values()):        
                print('password not change')

        form = SetPasswordForm(user)
        return render(request , self.template_name , locals()) 
         
    
class PasswordReset(View):
    template_name = 'pages/password_reset.html'
    
    def get(self , request):
        form = PasswordResetForm()
        return render(request , self.template_name , locals())
    
    def post(self , request):
        pass
    
class PasswordResetConfirm(View):
    
    def get(request):
        return redirect("home")
    
    
    
    
    

    



