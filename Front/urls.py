from django.urls import path
from Front.views import home , property , contact , profile , logout_form , register , loginform ,about , edit_profile , add_property

urlpatterns = [
    path('' , home , name="home"),
    path('property/' , property , name="property"),
    path('contact/' , contact , name="contact"),
    path('login/' , loginform , name="loginform"),
    path('about/' , about , name="about"),
    path('register/', register , name="register" ),
    path('logout/' , logout_form, name='logout'),
    path("profile/" , profile , name='profile'),
    path("edit/" , edit_profile , name='edit' ),
    path("add_property/" , add_property , name="add_property")

]