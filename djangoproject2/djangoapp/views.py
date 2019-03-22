from django.shortcuts import render
from django.http import HttpResponse
from djangoapp.models import AccessRecords, Topics, WebPage
from . import forms

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

def form_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print('NAME'+form.cleaned_data['name'])
            print('EMAIL'+form.cleaned_data['email'])
            print('TEXT'+form.cleaned_data['text'])
    return render(request, 'djangoapp/form.html', {'forms':form})
