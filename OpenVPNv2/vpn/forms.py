# -*- utf-8 -*-
__author__ = 'root'

from django.forms import ModelForm
from models import Certs
from django import forms
class CommentForm(ModelForm):
    class Meta:
        model = Certs
        fields = ['certs_user_name']

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea)

class GenerateCertUsr(forms.Form):
    name_certificate = forms.CharField(max_length=30,required=False)
    location_certificate = forms.CharField(required=False)
    send_email_certificate = forms.EmailField(required=False)

class RevokeCertUsr(forms.Form):
    name_certificate = forms.CharField(max_length=30,required=False)
    send_email_certificate = forms.EmailField(required=False)

