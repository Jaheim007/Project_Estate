from django.db import models

from Authentication.models import RepeatFields ,InactiveRepeatFields , City , Country

class Bedrooms(RepeatFields):
    number = models.CharField(max_length=150)
    
class Bathrooms(RepeatFields):
    number = models.CharField(max_length=150)
    
class AdditionalPropertyImage(RepeatFields):
    images = models.ImageField(upload_to="Additional_Images")
    
class Garage(RepeatFields):
    number = models.CharField(max_length=150)
    
    
class Properties(InactiveRepeatFields):
    name = models.CharField(max_length=150)
    price = models.CharField(max_length=150)
    city = models.ForeignKey(City, on_delete=models.SET_NULL , related_name='properties_city')
    country = models.ForeignKey(Country, on_delete=models.SET_NULL , related_name='properties_country')
    image = models.ImageField( upload_to='Property_images')
    
    
    
    
    
    
