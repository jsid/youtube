
from django.urls import path
from . import views

urlpatterns = [
    # form view
    path('newcontact/',views.ContactFormView.as_view(),name='newcontact'),
    path('thankyou/',views.ThanksTemplateView.as_view(),name='thankyou'),
    
    
    # crateview
    path('stucreate/',views.StudentCreateview.as_view(),name='stucreate'),
    path('ty/',views.ty.as_view(),name='ty'),
    path('detail/<int:pk>',views.DetailStudent.as_view(),name='detail'),
    
    
    # update
    path('update/<int:pk>',views.studentUpdateview.as_view(),name='update'),
    
    # delete
    path('delete/<int:pk>',views.Deleteviewstu.as_view(),name='delete'),
    
    
    
    
    
    
    path('accounts/profile/',views.profile,name='profile'),
    
    # form api
    path('form1/',views.showformdata,name='form1'),
    
]