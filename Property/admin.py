from django.contrib import admin

from Property import models

@admin.register(models.Bathrooms)
class Bathrooms(admin.ModelAdmin):
        list_display = (
            "number",
        )
        
@admin.register(models.Bedrooms)
class Bedrooms(admin.ModelAdmin):
        list_display = (
            "number",
        )
        
@admin.register(models.AdditionalPropertyImage)
class AdditionalPropertyImage(admin.ModelAdmin):
        list_display = (
            "image1",
            "image2",
            "image3",
            "image4",
            "image5"
        )

@admin.register(models.PropertyType)
class PropertyType(admin.ModelAdmin):
        list_display = (
            "property_types",
        )
    
@admin.register(models.Status)
class Status(admin.ModelAdmin):
        list_display = (
            "state",
        )
        
@admin.register(models.Properties)
class Properties(admin.ModelAdmin):
        list_display = (
            "name",
            "price",
            "status",
            "property_type",
            "garage",
            "bathrooms",
            "bathrooms",
            "country",
            "city",
            "address",
            
            
        )
     
@admin.register(models.Garage)
class Garage(admin.ModelAdmin):
        list_display = (
            "number",
        )
        


        
