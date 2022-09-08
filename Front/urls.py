from django.urls import path
from Front.views import home , property , contact , element , blog , register , login ,about

urlpatterns = [
    path('' , home , name="home"),
    path('property/' , property , name="property"),
    path('contact/' , contact , name="contact"),
    path('element' , element , name="element"),
    path('blog/' , blog , name="blog"),
    path('register/' , register , name="register"),
    path('login/' , login , name="login"),
    path('about/' , about , name="about"),
    path('register/', register , name="register" )

]