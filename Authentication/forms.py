from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import get_user_model

from Property.models import Properties

class NewUserForm(UserCreationForm): 
    email = forms.EmailField()
    
    class Meta: 
        model = get_user_model()
        fields = (
            "first_name",
            "last_name", 
            "username", 
            "email",
            "password1",
            "password2",
        )
        
class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=255, widget=forms.PasswordInput)
    
class UpdateProfile(ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = get_user_model()
        fields = [
            "first_name" , 
            "last_name", 
            "username", 
            "email",
            "image",
            "phone_number",
        ]
    
class AddProperty(ModelForm):
    class Meta:
        model = Properties
        fields = [
            'name', 
            'price',
            'property_type',
            'bedroom',
            'bathroom',
            'garage',
            'country',
            'address_name',
            'main_image', 
        ]

    

        

    

