from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from .models import *
# Create your views here.

@csrf_exempt
def register(request):
    if request.method=='POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')

        if password == cpassword:
            user = users(first_name=fname,last_name=lname,email=email,contact=contact,password=password)
            user.save()
            enter = "success"
            context = {'enter':enter}
            return render(request,"expense/login.html",context)
        else:
            enter = "error"
            context = {'enter': enter}
            return render(request,"expense/register.html",context)
    return render(request,'expense/register.html',context=None)

@csrf_exempt
def login(request):
    return render(request,'expense/login.html',context=None)

@csrf_exempt
def  dashboard(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

