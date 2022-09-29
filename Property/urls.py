from django.urls import path
from Property import views


urlpatterns = [
    path('property/' , views.Property.as_view() , name='property'),
    path('myproperty/' , views.MyProperty.as_view() , name='myproperty'),
    path('single/' , views.SingleProperty.as_view(), name='single')
]