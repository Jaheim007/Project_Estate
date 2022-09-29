from dataclasses import fields
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm , PasswordResetForm
from django.contrib.auth import get_user_model
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

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
        
class EditProfile(ModelForm):
    class Meta:
        model = get_user_model()
        fields = [
            "first_name" , 
            "last_name", 
            "username", 
            "phone_number",
            "image",
        ]
    
class AddProperty(ModelForm):
    class Meta:
        model = Properties
        fields = [
            'name', 
            'price',
            'status',
            'property_type',
            'bedroom',
            'bathroom',
            'garage',
            'address_name',
            'description',
            'main_image'
        ]
        
class ChangePassword(SetPasswordForm):
    class Meta:
        model = get_user_model()
        fields = [
            'new_password1', 
            'new_password2'
        ]
    

        

    

