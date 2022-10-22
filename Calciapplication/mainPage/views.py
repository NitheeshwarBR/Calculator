from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'login.html')
def login(request):
    return render(request,'page.html')
def signup(request):
    return render(request,'signup.html')
def backlogin(request):
    return HttpResponseRedirect('/')
def home(request):
    return render(request,'page.html')
