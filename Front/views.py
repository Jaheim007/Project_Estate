from django.shortcuts import render 
from django.views.generic import View


class Home(View):
    template_name = 'pages/index.html'
    
    def get(self , request):
        return render(request , self.template_name , locals())
    
    def post(self , request): 
        pass
  
    
class Contact(View):
    template_name = 'pages/contact.html'
    
    def get(self , request):
        return render(request , self.template_name , locals())
    
    def post(self , request):
        pass
   
    
class About(View):
    template_name = 'pages/about.html'
    
    def get(self , request):
        return render(request , self.template_name , locals())
    
    def post(self , request):
        pass 
    





