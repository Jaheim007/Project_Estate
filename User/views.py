from django.shortcuts import render
from django.views.generic import View

from User import forms
from Property import models

class AddProperty(View):
    template_name = 'pages/add_property.html'
    class_form = forms.AddProperty
    
    def get(self , request):
        pass

    def post(self , request):
        form = self.class_form
        name = request.POST.get("name")
        price = request.POST.get("price")
        users = request.user
        
        print(request.user)
         
        property = models.Properties(
            name = name, 
            price = price,
            users = users
        )
        
        property.save()
    
        return render(request , "pages/add_property.html" , locals())
        