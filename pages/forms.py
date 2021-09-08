from django import forms
from django.forms.widgets import Textarea

class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email_address = forms.EmailField(max_length=150)
    subject = forms.CharField(max_length=150)
    message = forms.CharField(widget=Textarea, max_length=2000)