from django.urls import path
from Front import views


urlpatterns = [
    path('' , views.Home.as_view() , name="home"),
    path('contact/' , views.Contact.as_view() , name="contact"),
    path('about/' , views.About.as_view() , name="about"),
]

