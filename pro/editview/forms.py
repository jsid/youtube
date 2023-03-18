# use of form api
from django import forms


class ContactForm(forms.Form):
    name=forms.CharField()
    email=forms.CharField()
    msg=forms.CharField(widget=forms.Textarea)
    
    
class StudentReg(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()