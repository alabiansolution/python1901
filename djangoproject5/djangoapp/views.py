from django.shortcuts import render
from djangoapp import forms
from djangoapp.models import Post

# Create your views here.

def index(request):
    home_view = {'home' : 'Welcome to my home page'}
    return render(request, 'djangoapp/index.html', context=home_view)

def post(request):
    post_form = forms.Post()
    if request.method == 'POST':
        post_form = forms.Post(request.POST)
        if post_form.is_valid():
           post_form.save(commit=True)
    return render(request, 'djangoapp/post.html', {'my_post' : post_form})

# def contactus(request):
#     contact_form = forms.ContactUsForm()
#     return render(request, 'djangoapp/contact.html', {'my_form' : contact_form})


def contactus(request):
    contact_form = forms.ContactUsForm()

    if request.method == 'POST':
        submit_form = forms.ContactUsForm(request.POST)
        if submit_form.is_valid():
            print("FORM ADDED")
            print("Name "+submit_form.cleaned_data['name'])
            print("Email "+submit_form.cleaned_data['email'])
            print("URL "+submit_form.cleaned_data['url'])
            print("Botcatcher "+submit_form.cleaned_data['botcatcher'])
            print("Message "+submit_form.cleaned_data['message'])

    return render(request, 'djangoapp/contact.html', {'my_form' : contact_form})
