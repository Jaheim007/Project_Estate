from django.db import models

from Authentication.models import RepeatFields , InactiveRepeatFields , Cities , Country

class PropertyType(RepeatFields):
    HOUSE = 'HOUSE'
    APARTMENT = 'APARTMENT'
    VILLAS = 'VILLA'
    STUDIO = 'STUDIO'
    OFFICE = 'OFFICE'
    
    TYPE = [
        (HOUSE , 'House'),
        (APARTMENT , 'Apartment'),
        (VILLAS , 'Villa'),
        (STUDIO , 'Studio'), 
        (OFFICE , 'Office')
    ]
    property_types = models.CharField(choices=TYPE , max_length=150)
    
class Status(RepeatFields):
    FOR_RENT = 'FOR RENT'
    FOR_SALE = 'FOR SALE'
    
    STATUS = [
        (FOR_RENT , 'For Rent'),
        (FOR_SALE , 'For Sale')
    ]
    state = models.CharField(choices=STATUS , max_length=254)

class Bedrooms(RepeatFields):
    number = models.CharField(max_length=150)
    
class Bathrooms(RepeatFields):
    number = models.CharField(max_length=150)

class Garage(RepeatFields):
    number = models.CharField(max_length=150)
    
class AdditionalPropertyImage(RepeatFields):
    image1 = models.ImageField(upload_to="Additional_Images")
    image2 = models.ImageField(upload_to="Additional_Images")
    image3 = models.ImageField(upload_to="Additional_Images")
    image4 = models.ImageField(upload_to="Additional_Images")
    image5 = models.ImageField(upload_to="Additional_Images")

class Properties(InactiveRepeatFields):
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.ForeignKey(Status,  on_delete=models.SET_NULL , null=True , related_name='property_status')
    property_type = models.ForeignKey(PropertyType, on_delete=models.SET_NULL , null=True , related_name='property_type')
    city = models.ForeignKey(Cities, on_delete=models.SET_NULL , null=True, related_name='properties_city')
    country = models.ForeignKey(Country, on_delete=models.SET_NULL ,null=True, related_name='properties_country')
    address = models.CharField(max_length=150)
    garage = models.PositiveIntegerField(default=0)
    bathrooms = models.PositiveIntegerField(default=0)
    bedrooms = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='Property_images')
    additional_images = models.ForeignKey(AdditionalPropertyImage ,  on_delete=models.SET_NULL , null=True , blank=True)
    
    
    
    
    
    
    
