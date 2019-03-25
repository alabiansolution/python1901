from django import forms
from django.core import validators
from djangoapp.models import Post

class ContactUsForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    url = forms.URLField()
    message = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput,
                      validators=[validators.MaxLengthValidator(0)])

class Post(forms.ModelForm):
    class Meta():
        model = Post
        fields = '__all__'









    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data["botcatcher"]
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError("There is an error")
    #     return botcatcher
