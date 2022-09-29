from django.shortcuts import render
from django.views.generic import View

from Property import models


class Property(View):
    template_name = 'pages/property.html'
    
    def get(self , request):
        properties = models.Properties.objects.all()
        return render(request , self.template_name , locals())
    
    def post(self , request): 
        pass

class SingleProperty(View):
    template_name = 'pages/single_property.html'
    
    def get(self , request):
        return render(request , self.template_name , locals())
    
    def post(self , request): 
        pass
