from django.shortcuts import render
from djangoapp.models import Topic, WebUserModel
from djangoapp import forms

# Create your views here.

def index(request):
    queryTable = WebUserModel.objects.all()
    homedict = {'home_content' : queryTable}
    return render(request, 'djangoapp/index.html', context=homedict)

def form_view(request):
    formvar = forms.FormName()
    return render(request, 'djangoapp/form.html', {'form' : formvar})
