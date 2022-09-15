from django.db import models

from Authentication.models import RepeatFields , InactiveRepeatFields , User

class AdditionalPropertyImage(RepeatFields):
    image1 = models.ImageField(upload_to="Additional_Images")
    image2 = models.ImageField(upload_to="Additional_Images")
    image3 = models.ImageField(upload_to="Additional_Images")
    image4 = models.ImageField(upload_to="Additional_Images")
    image5 = models.ImageField(upload_to="Additional_Images")
    
    def __str__(self):
        return self.image1

class Countries(RepeatFields):
    country = models.CharField(max_length=150)
    
    def __str__(self):
        return self.country

class Bedrooms(RepeatFields):
    number = models.CharField(max_length=150)
    
    def __str__(self):
        return self.number
    
class Bathrooms(RepeatFields):
    number = models.CharField(max_length=150)
    
    def __str__(self):
        return self.number
    
class Garages(RepeatFields):
    number = models.CharField(max_length=150)
    
    def __str__(self):
        return self.number
    
class PropertyTypes(RepeatFields):
    FOR_SALE = "FOR SALE"
    FOR_RENT = "FOR RENT"
    
    TYPE = [
        (FOR_SALE , "For Sale"),
        (FOR_RENT , "For Rent")
    ]
    
    type = models.CharField(choices=TYPE , max_length=150)
    
    def __str__(self):
        return self.type

class Properties(User):
    name = models.CharField(max_length=150)
    price = models.CharField(max_length=150)
    property_type = models.ForeignKey(PropertyTypes ,  on_delete=models.SET_NULL , null=True , related_name="properties_property_type")
    bedroom = models.ForeignKey(Bedrooms, on_delete=models.SET_NULL , null=True , related_name="properties_bedrooms")
    bathroom = models.ForeignKey(Bathrooms, on_delete=models.SET_NULL , null=True , related_name="properties_bathrooms")
    garage = models.ForeignKey(Garages, on_delete=models.SET_NULL , null=True , related_name="properties_garages")
    country = models.ForeignKey(Countries, on_delete=models.SET_NULL ,null=True, related_name='properties_country')
    address_name = models.CharField(max_length=150)
    main_image = models.ImageField( upload_to='Property_images')
    user = models.ForeignKey(User , on_delete=models.SET_NULL , null=True)
    
    def __str__(self):
        return self.name

    
    
    
    
    
    
    
    
