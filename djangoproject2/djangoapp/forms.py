from django import forms
from django.core import validators

def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("Name must start with z")
class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Enter Email again")
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(widget=forms.HiddenInput, required=False,
                                validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data = super().clean()
        amail = all_clean_data['email']
        vmail = all_clean_data['verify_email']
        if amail != vmail:
            raise forms.ValidationError('MAKE SURE EMAILS MATCH')
