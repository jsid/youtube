from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('func/',views.myView,name='func'),
    path('cl/',views.MyView.as_view(),name='cl'),
    path('subcl/',views.MyviewChild.as_view(name='ironheart'),name='subcl'),
    
    
    # new class
    path('home/',views.NewHome.as_view(),name='home'),
    path('contact/',views.contact,name='contact'),
    path('ContactView/',views.ContactView.as_view(),name='ContactView'),
    
    # template view
    path('t1/',views.TemplateView.as_view(template_name='t1.html'),name='t1'),
    path('t2/',views.Hometemp.as_view(extra_context={'code':'ironheart'}),name='t2'),
    path('t3/<int:id>/',views.Hometemp.as_view(),name='t3'),
    
    # redirect view
    path('r1/',views.RedirectView.as_view(url='https://instagram.com'),name='r1'),
    path('sid/',views.sid.as_view(),name='sid'),
    
]