from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def index(request):
#     return HttpResponse("Home Page")

def index(request):
    homedict = {'index_content' : 'Home Page'}
    return render(request, 'djangoapp1/index.html', context= homedict)

def contact(request):
    contactdict = {'contact_con' : 'Contact Us'}
    return render(request, 'djangoapp1/contact.html', context= contactdict)


def about(request):
    aboutdict = {'about_content' : 'About Us'}
    return render(request, 'djangoapp1/about.html', context= aboutdict)
