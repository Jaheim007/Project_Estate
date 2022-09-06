
from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

class InactiveRepeatFields(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    inactive = models.BooleanField(default=False)
    
class RepeatFields(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Country(RepeatFields): 
    name = models.CharField(max_length=150)
    
class City(RepeatFields):
    name = models.CharField(max_length=150)

class User(AbstractUser, InactiveRepeatFields): 
    AGENT = 'AG'
    CLIENT = 'CL'
    
    USER_TYPE = [
        (AGENT , 'Agent'),
        (CLIENT , 'Client')
    ]

    image = models.ImageField(upload_to='User__Images', blank=True)
    phone_number = PhoneNumberField()
    city = models.ForeignKey(City , on_delete=models.SET_NULL ,null=True , related_name="user_city")
    country = models.ForeignKey(Country , on_delete=models.SET_NULL ,null=True , related_name="user_country")
    description = models.TextField()
    occupation = models.CharField(max_length=150)
    user_type = models.CharField(choices=USER_TYPE , max_length=50)    
    address = models.TextField()
    facebook = models.URLField()
    instagram = models.URLField()
    twitter = models.URLField()
    linkedin = models.URLField()
    
    
    
