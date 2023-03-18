from django import forms
from django import forms
class ContactForm(forms.Form):
    name=forms.CharField(max_length=17)