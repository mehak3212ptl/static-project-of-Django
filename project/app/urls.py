from django.urls import path
from .views import*

urlpatterns = [
    path('',home,name='home'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('blog/',blog,name='blog'),
    path('protfolio/',protfolio,name='protfolio')

    
    
]