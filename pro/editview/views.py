from django.shortcuts import render
from django import forms
from .models import *
from .forms import *
# Create your views here.
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
class ContactFormView(FormView):
    template_name='editview/contact.html'
    form_class=ContactForm
    success_url='/thankyou/'
    
    def form_valid(self,form):
        print(form)
        print(form.cleaned_data['name'])
        print(form.cleaned_data['email'])
        print(form.cleaned_data['msg'])
        
        return super().form_valid(form)
    
class ThanksTemplateView(TemplateView):
    template_name='editview/thankyou.html'
    
    
    
    
#####################Create views ############    # 
from django.views.generic.edit import CreateView
    
class StudentCreateview(CreateView):
    model=Student
    fields=['name','email','password']
    # success_url='/ty/'
    # adding bootstrap class
    def get_form(self):#getting form
        form = super().get_form()
        form.fields['name'].widget=forms.TextInput(attrs={'class':'myclass mb-3 bg-primary'})
        form.fields['password'].widget=forms.PasswordInput(attrs={'class':'mypass'})
        
        return form

    
class ty(TemplateView):
    template_name='editview/thankyou.html'
 


class DetailStudent(DetailView):
    model=Student
    
    
    
    
from django.views.generic.edit import UpdateView
# update view
class studentUpdateview(UpdateView):
    model=Student
    fields=['name','email','password']
    success_url='/ty/'
    
    
# delete views
from django.views.generic.edit import DeleteView
class Deleteviewstu(DeleteView):
    model=Student
    success_url='/stucreate/'
    

# authentication view
def profile(request):
    return render(request,'registration/profile.html')


# form api
def showformdata(request):
    fm=StudentReg(auto_id='sid_%s',label_suffix='$==',initial={'name':'ironheart','email':'iron@gmail.com'})
    fm.order_fields(field_order=['email','name'])
    # print(fm)
    return render(request,'editview/form1.html',locals())


