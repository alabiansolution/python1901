from django.shortcuts import render
from django.http import HttpResponse
from djangoapp.models import AccessRecords, Topics, WebPage

# Create your views here.

def index(request):
    homepageslist = WebPage.objects.all()
    homedict = {'home_content' : homepageslist}
    return render(request, 'djangoapp/index.html', context=homedict)

def about(request):
    aboutdict = {
                'about_heading' : 'About Us',
                'about_content' : 'My About Us content'
               }
    return render(request, 'djangoapp/about.html', context=aboutdict)
