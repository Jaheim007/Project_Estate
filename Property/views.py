from django.shortcuts import render
from django.views.generic import View


class Property(View):
    template_name = 'pages/property.html'
    
    def get(self , request):
        return render(request , self.template_name , locals())
    
    def post(self , request): 
        pass

class SingleProperty(View):
    template_name = 'pages/single_property.html'
    
    def get(self , request):
        return render(request , self.template_name , locals())
    
    def post(self , request): 
        pass
