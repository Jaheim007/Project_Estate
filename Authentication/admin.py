from django.contrib import admin
from Authentication import models

@admin.register(models.User)

class User(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name", 
        "username", 
        "email",
        "user_type" 
    )