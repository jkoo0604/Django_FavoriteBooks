from django.shortcuts import render, redirect
import bcrypt
from .models import User
from django.contrib import messages
from django.http import JsonResponse
import re


# Create your views here.
def index(request):
    if 'userid' in request.session:
        user = User.objects.filter(id=request.session['userid'])
        if user:
            return redirect('/book')
    return render(request,'index.html')

def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect('/')
    
    password = request.POST['password']
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    newuser = User.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'],password=pw_hash)
    request.session['userid'] = newuser.id
    return redirect('/book')


def login(request):
    errors = User.objects.pw_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect('/')
    user = User.objects.filter(email=request.POST['logemail']) 
    logged_user = user[0]   
    request.session['userid'] = logged_user.id
    return redirect('/book')

def success(request):
    if 'userid' in request.session:
        context = {
            'current_user': User.objects.get(id=request.session['userid'])
        }
        return render(request,'welcome.html',context)
    return redirect('/')


def logout(request):
    request.session.flush()
    return redirect('/')


def testunique(request):
    email = request.GET.get("email", None)
    print(email)
    if User.objects.filter(email__iexact=email).exists():
        return JsonResponse({"used":True}, status = 200)
    else:
        return JsonResponse({"used":False}, status = 200)
    
    return JsonResponse({}, status = 400)

def testlogin(request):
    errors = User.objects.pw_validator(request.POST)
    print(errors)
    if len(errors)>0:
        return JsonResponse({"match":False}, status = 200)
    else:
        return JsonResponse({"match":True}, status = 200)
