from django.urls import path
from .views import*

urlpatterns = [
    path('',home,name='home'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('blog/',blog,name='blog'),
    path('protfolio/',protfolio,name='protfolio'),
    path('port2/',port2,name='port2'),
    path('port3/',port3,name='port3'),
    path('steps/',steps,name='steps'),
    path('succesfull/',success,name='success'),
    path('sign/',sign,name='sign'),
    path('login/',login,name='login')
    
]