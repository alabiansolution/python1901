from django.shortcuts import render

# Create your views here.

def index(request):
    homedict = {'home_content' : 'Welcome to home page'}
    return render(request, 'djangoapp/index.html', context=homedict)


def about(request):
    aboutdict = {'about_content' : 'Welcome to about us'}
    return render(request, 'djangoapp/about.html', context=aboutdict)
