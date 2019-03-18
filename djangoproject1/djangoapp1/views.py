from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Home Page")

def about(request):
    aboutdict = {'about_content' : 'About Us'}
    return render(request, 'djangoapp1/about.html', context= aboutdict)
