from django.shortcuts import render

def home(request):
    return render(request, "pages/index.html" , locals())

def property(request):
    return render(request , "pages/property.html" , locals())

def contact(request):
    return render(request , "pages/contact.html" , locals())

def about(request):
    return render(request , "pages/about.html" , locals())

def element(request):
    return render(request , "pages/elements.html" , locals())

def login(request):
    return render(request , "pages/login.html" , locals())

def register(request):
    return render(request , "pages/register.html" , locals())

def blog(request):
    return render(request , 'pages/blog.html', locals())

def about(request):
    return render(request , 'pages/about.html' , locals())







# Create your views here.
