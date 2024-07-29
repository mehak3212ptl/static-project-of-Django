from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def blog(request):
    return render(request,'blog.html')

def contact(request):
    return render(request,'contact.html')

def protfolio(request):
    return render(request,'protfolio.html')

def port2(request):
    return render(request,'port2.html')

def port3(request):
    return render(request,'port3.html')

def steps(request):
    return render(request,'steps.html')
