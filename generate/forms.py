__author__ = 'arya'
from django import forms

class StarterPackForm(forms.Form):
    title = forms.CharField(max_length=30)
    link1 = forms.CharField(max_length=200)
    link2 = forms.CharField(max_length=200)
    link3 = forms.CharField(max_length=200)
    link4 = forms.CharField(max_length=200)