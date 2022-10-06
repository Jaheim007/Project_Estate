from django.shortcuts import render 
from django.views.generic import View
from django.http import JsonResponse

from Front import models
from Property import models


class Home(View):
    template_name = 'pages/index.html'
    
    def get(self , request):
        properties = models.Properties.objects.all()
        return render(request , self.template_name , locals())
    
    def post(self , request): 
        msg =''
        success = True
        if request.method == "POST":
            email = request.POST.get("email")

        
        newsletter = models.Newsletters(
            email = email
        )
        
        newsletter.save()
        msg = 'Your email has been saved, we will keep you updated on our latest info.'
        
        data = {
        'msg': msg,
        'success': success
        }

        return JsonResponse(data, safe=False)
        
    
class Contact(View):
    template_name = 'pages/contact.html'
    
    def get(self , request):
        return render(request , self.template_name , locals())
    
    def post(self , request):
        msg =''
        success = True

        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        
        contact = models.Contact(
            name = name, 
            email = email, 
            subject = subject, 
            message = message
        )
        
        contact.save()
        msg = 'Thank you for contacting Medicio.'
        
        data = {
        'msg': msg,
        'success': success
        }

        return JsonResponse(data, safe=False)
   
    
class About(View):
    template_name = 'pages/about.html'
    
    def get(self , request):
        return render(request , self.template_name , locals())
    
    def post(self , request):
        pass






