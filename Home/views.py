from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User
from .models import *
import random
from django.contrib.auth import get_user_model

User=get_user_model()
# Create your views here.
def home_page(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        password=request.POST.get('password')
        user=User(email=email,username=username)
        user.save()
        otp=str(random.randint(1000,9999))
        Profile(user=user,mobile=mobile,otp=otp)




       
    return render(request, 'register.html')

def Otp(request):
    return render(request, 'otp_with.html')