from re import template
from django.shortcuts import render
from .models import *
# Create your views here.
# Generic based views
# List view
from django.views.generic.list import ListView



class studentListView(ListView):
    model=Student #it gives student.objects.all in one line
    # it return default template and default context
    
# with using differnt/custom template and context
class newstudentListView(ListView):
 
    model=Student
    # template_name_suffix='_get' #it will be changeable
    ordering=['roll'] #set the order of data
    template_name='practice/new.html'#custom template
    context_object_name='stu' #custom context name
    '''some methods:'''
    
    #RETURNS a filter query set
    def get_queryset(self):
        return Student.objects.filter(course='MBA')
    
    # creating new context
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['fresher']=Student.objects.all().order_by('name')
        return context
    
    # dynamic template render
    # def get_template_names(self):
    #     if self.request.COOKIES['user']=='sonam':
    #         template_name='practice/sonam.html'
    #     else:
    #         template_name=self.template_name
    #     return[template_name]
  
            
# ####################Detail view###################
from django.views.generic.detail import DetailView

class stuDetailView(DetailView):
    model=Student  
    # template_name='practice/det.html'
    # for searching for id based
    # pk_url_kwarg='id'
    