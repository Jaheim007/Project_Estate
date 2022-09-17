from django.contrib import admin

from Property import models

@admin.register(models.Countries)
class Countries(admin.ModelAdmin):
    list_display = (
        'country',
    )
@admin.register(models.Bathrooms)
class Bathrooms(admin.ModelAdmin):
    list_display = (
        'number',
    )
    
@admin.register(models.Bedrooms)
class Bedrooms(admin.ModelAdmin):
    list_display = (
        'number',
    )
    
@admin.register(models.Garages)
class Garages(admin.ModelAdmin):
    list_display = (
        'number',
    )

@admin.register(models.PropertyTypes)
class PropertyTypes(admin.ModelAdmin):
    list_display = (
        type,
    )

@admin.register(models.Properties)
class Properties(admin.ModelAdmin):
    list_display = (
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
    )