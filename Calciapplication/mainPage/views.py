from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate,login,get_user_model
# Create your views here.
def index(request):
    return render(request,'login.html')
def Loginpage(request):
    if request.method=='POST':
        username=request.POST["emailid"]
        password=request.POST["pass"]
        if username==get_user_model("username") and password==get_user_model("password1"):
            return render(request,"page.html")
        else:
            messages.error(request,"invalid credentials!!!")
            return render(request,"login.html")
    else:
        return render(request,"login.html")
    
def signup(request):
    if request.method=="POST":
        firstname=request.POST.get('fname')
        lastname=request.POST.get('lname')
        username=request.POST.get('emailid')
        password1=request.POST.get('pass1')
        password2=request.POST.get('pass2')
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"user already exists!!!")
            else:
                user=User.objects.create_user(username=username,password=password2)
                user.first_name=firstname
                user.last_name=lastname
                user.save()
                print("user created")
                return render(request,"login.html")
        else:
            messages.error(request,"invalid password!!!")
            return render(request,"signup.html")
        
    else:
        print("user not created!!!")
        return render(request,"signup.html")
def backlogin(request):
    return HttpResponseRedirect('/')
def home(request):
    return render(request,'page.html')
