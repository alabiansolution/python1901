from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Welcome to my site")

def about(request):
    aboutdict = {'about_content':'About Us'}
    return render(request, 'djangoapp/about.html', context=aboutdict)
