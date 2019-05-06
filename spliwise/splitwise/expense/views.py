from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.shortcuts import redirect
from datetime import *
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
    try:
        request.session['name']
    except KeyError:
        return redirect('/login/')
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        u = users.objects.get(email=username)
        if u.password == password:
            request.session['name']= u.first_name
            request.session['email']= u.email
            request.session['user_id']= u.user_id
            context= {'user_id':request.session['user_id'],'name':request.session['name']}
            return render(request,'expense/dashboard.html',context)
            #return redirect('/dashboard/')
        else:
            error = "incorrect"
            context = {'error':error}
            return render(request,'expense/login.html',context)
    else:
        if request.session['name']:
            context = {'user_id': request.session['user_id'], 'name': request.session['name']}
            return render(request, 'expense/dashboard.html', context)

@csrf_exempt
def expense(request):
    try:
        request.session['name']
    except KeyError:
        return redirect('/login/')
    if request.method =='POST' and request.session['name']:
        user = users.objects.get(user_id=request.session['user_id'])
        title = request.POST.get('title')
        description = request.POST.get('description')
        amount = request.POST.get('amount')
        d = datetime.today()
        bill = expenses(euser_id=user , title=title , description=description , amount=amount , date=d.strftime('%Y-%m-%d %H:%M:%S'))
        bill.save()
        exp=expenses.objects.filter(euser_id=user)
        context = {'name': request.session['name'] , 'exp':exp}
        return render(request, 'expense/expenses.html', context)
    if request.session['name']:
        user = users.objects.get(user_id=request.session['user_id'])
        exp = expenses.objects.filter(euser_id=user)
        context = {'name':request.session['name'],'exp':exp}
        return render(request,'expense/expenses.html',context)


@csrf_exempt
def split(request):
    return render(request,'expense/split.html',context=None)

@csrf_exempt
def buddy(request):
    return render(request,'expense/buddys.html',context=None)

@csrf_exempt
def logout(request):
    request.session.modified = True
    del(request.session['name'])
    del(request.session['email'])
    del(request.session['user_id'])
    return render(request, 'expense/login.html', context=None)
