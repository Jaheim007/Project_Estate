from django.urls import path
from Property import views


urlpatterns = [
    path('property/' , views.Property.as_view() , name='property'),
    
]