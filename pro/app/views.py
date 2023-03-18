from django.http import HttpResponse
from django.shortcuts import render
from django.urls import is_valid_path

from pytube import *

from django.views import View
from .forms import ContactForm

# trmplate view
from django.views.generic.base import TemplateView
# Create your views here.
# defining function


def index(request):
    # checking the link in post or not
    if request.method == 'POST':
        # getting link from frontend
        link = request.POST['link']
        video = YouTube(link)

        # setting video resolution
        stream = video.streams.get_highest_resolution()

        # file1=open('videos','w')
        # print(file1,'opened')
        # download video
        result = stream.download()
        print(result)
        # returning html page
        return render(request, 'index.html')

    return render(request, 'index.html')


# function based view
def myView(request):
    # by default method is get
    return HttpResponse('<h1>function based view </h1>')

# class based view


class MyView(View):
    # we need to define the method in class based view
    name = 'siddhant'

    def get(self, request):
        return HttpResponse(self.name)

# inheeritance of above class
# and accessing its attribute        #


class MyviewChild(MyView):
    def get(self, request):
        return HttpResponse(self.name)


# new classes
class NewHome(View):
    def get(self, request):
        context = {'name': 'siddhant'}
        print('done')
        return render(request, 'home.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse('<h3>done</h3>')
    else:
        form = ContactForm()
        print('else')
        return render(request, 'contact.html', {'form': form})


class ContactView(View):
    def get(self, request):
        form = ContactForm()
        print('else')
        return render(request, 'contact.html', {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse('<h3>done</h3>')


# template view with context 
class Hometemp(TemplateView):
    template_name= 't2.html'
        
    def get_context_data(self, **kwargs) :
        context=super().get_context_data(**kwargs)
        context['name']='sid'
        context['roll']=123
        print(context)
        print(kwargs)
        return context
    
from django.views.generic.base import RedirectView
# redirect view
class sid(RedirectView):
    url='https://en.wikipedia.org/wiki/Iron_Man_(2008_film)'