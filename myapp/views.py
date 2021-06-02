from django.shortcuts import render
from .models import Make_appoint,User
from django.conf import settings
from django.core.mail import send_mail
import random

# Create your views here.
def index(request):
    return render(request,'index.html')

def signup(request):
    if request.method=="POST":
        try:
            user=User.objects.get(email=request.POST['email'])
            msg="Email Already Registered, You can Appointment Directly."
            return render(request,'signup.html',{'msg':msg})
        except:
            User.objects.create(
                fname=request.POST['fname'],
                lname=request.POST['lname'],
                email=request.POST['email'],
                gender=request.POST['gender'],
                phone=request.POST['phone'],
                address=request.POST['address']
            )
            msg="User Signup Successfully.."
            return render(request,'make_appoint.html',{'msg':msg})
    else:
        return render(request,'signup.html')

def make_appoint(request):
    if request.method=="POST":
        Make_appoint.objects.create(
                name=request.POST['name'],
                email=request.POST['email'],
                date=request.POST['date'],
                dept=request.POST['dept'],
                phone=request.POST['phone'],
                message=request.POST['message']
            )
        subject = 'OTP for Appointment.'
        otp=random.randint(1000,9999)
        message = "Your OTP for Appointment is "+str(otp)
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [request.POST['email'],]
        send_mail( subject, message, email_from, recipient_list )
        return render(request,'otp.html',{'otp':otp,'email':request.POST['email']})
    else: 
        return render(request,'make_appoint.html')

def verify_otp(request):
    otp1=request.POST['otp1']
    otp2=request.POST['otp2']
    email=request.POST['email']
    if otp1==otp2:
        subject = 'Health care Appointment Book .'
        message = "Your Appointment successfully booked , You can visit our center for your booking date."
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [request.POST['email'],]
        send_mail( subject, message, email_from, recipient_list )
        msg="Your Appointment booked Successfully"
        return render(request,'make_appoint.html',{'msg':msg})
    else:
        msg="Invalid OTP"
        return render(request,'otp.html',{'otp':otp1,'email':email,'msg':msg})  