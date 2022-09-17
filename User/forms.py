from django.forms import ModelForm

from Property import models

class AddProperty(ModelForm):
    class Meta:
        model = models.Properties
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
            'users'
        ]