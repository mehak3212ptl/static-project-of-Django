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

def success(request):
    return render(request,'success.html')

def sign(request):
    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        response=render(request,'success.html')
        response.set_cookie('fname',fname)
        response.set_cookie('lname',lname)
        response.set_cookie('email',email)
        return response
    return render(request,'sign.html')

def login(request):
    if request.method=='POST':
        fname=request.POST.get('fname')
        email=request.POST.get('email')
        print(fname,email)
        response=render(request,'home.html')
        fname=request.COOKIES['fname']
        email=request.COOKIES['email']
        if email==email:
            data={
                'fname':fname,
                'email':email
                }
        return render(request,'success.html',data)
    return render(request,'login.html')

