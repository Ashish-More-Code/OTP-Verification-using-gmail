from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model,authenticate,login,logout
from django.contrib import messages
from .emailer import *
from .models import *
import random

# Create your views here.
def home(request):
    if request.method=='POST':
        mobilenumber=request.POST['mobilenumber']
        password=request.POST['password']
        user=authenticate(phone_number=mobilenumber,password=password)
        if user is not None:
            login(request, user)
            uphone=request.user.phone_number
            user_obj=myuser.objects.filter(phone_number=uphone)
            if not user_obj.exists():
                return redirect('/')
            
            otp=random.randint(1000,9999)
            user_obj.update(otp=otp)
            email=user_obj[0].email
            subject="OTP for login"
            message=f"your OTP is {otp}"
            send_otp_on_email(email,subject,message)
            messages.error(request, "login completed")
            return redirect(f'/checkotp/{user_obj[0].id}')
        else:
            messages.error(request, "user not exists")
            return redirect('/')
    else:
        return render(request,'login.html')


def register(request):
    if request.method=='POST':
        email=request.POST['email']
        phonenumber=request.POST['mobilenumber']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        password=request.POST['password']
        if email=="" or phonenumber=="" or firstname=="" or lastname=="" or password=="":
            messages.error(request, "Fields cannot be empty.")
            return redirect('/register')
        else:
            user=get_user_model().objects.create(email=email,first_name=firstname,last_name=lastname,phone_number=phonenumber)
            user.set_password(password)
            user.save()
            return redirect('/')
    else:
        return render(request,'signup.html')
    
def signout(request):
    logout(request)
    return redirect('/')

def checkOtp(request,id):
    if request.method=='POST':
        otp=request.POST['otp']
        user_obj=myuser.objects.get(id=id)
        if int(otp)==user_obj.otp:
            return redirect('/dashboard')
        else:
            messages.error(request, "Invalid otp.")
            return redirect(f'/checkotp/{user_obj.id}')
    return render(request,'verifyotp.html')


def dashbord(request):
    messages.error(request, "user login is successful")
    return render(request,'dashboard.html')
