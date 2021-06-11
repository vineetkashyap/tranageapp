from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
import math, random
from django.conf import settings
from django.template.loader import render_to_string
from django.http import JsonResponse, request
from django.core.mail import EmailMessage


def generateOTP() :
     digits = "0123456789"
     OTP = ""
     for i in range(4) :
         OTP += digits[math.floor(random.random() * 10)]
     return OTP

def send_email_otp(request):
     email=request.GET.get   ("email")
     print(email)
     o=generateOTP()
     print("=====================================>EMail-OTP : ",o)
     email =EmailMessage (
            'We got a quary',
            'Your Verification OTP is '+str(o),
            settings.EMAIL_HOST_USER,
            [request.POST['email']],
        )
     email.fail_silently=False
     email.send()
     return JsonResponse({'o':o,"status":"success"})




from twilio.rest import Client

def send_mobile_otp(request):
    # account_sid = "AC82baaae2ec5a11e204d15b23bcc04fad"
    # auth_token = "2508bb9b64305c9c788f884de428083d"
    # client = Client(account_sid, auth_token)
    o=generateOTP()
    print("=====================================>Mobile-OTP : ",o)
    # message = client.messages.create(
    #                     body="Your Verification OTP is : "+str(o),
    #                     from_='+19706707531',
    #                     to='+917905637810'
    #                 )
    return JsonResponse({'o':o,"status":"success"})
