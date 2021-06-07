from django import template
from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from dashboard.models import Add_update
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, logout,login
from app.models import Distributor_Model,Investor_Model
from django.http import JsonResponse, request
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import EmailMessage,send_mass_mail
from django.conf import settings
from django.template.loader import render_to_string

# Create your views here.
def index (request):
    card = Add_update.objects.all()
    return render(request,'index.html',{'cards':card})
    
def about (request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def team(request):
    return render(request,'team.html')

def service(request):
    return render(request,'services.html')

def partner(request):
    return render(request,'partner.html')

def  blog(request):
    return render(request,'blog.html')


def registration(request):
    return render(request,'registrationform.html')


def product(request):
    return render(request,'productpage.html')
@csrf_exempt
def distributor(request):
     if request.method == "POST":
        full_name = request.POST.get('name')
        father_name = request.POST.get('fathername')
        date_of_birth = request.POST.get('dateplaceholder')
        aadhar_no= request.POST.get('aadhar')
        pan_no= request.POST.get('pancard')
        education= request.POST.get('education')
        occupation = request.POST.get('occupation')
        residential_address = request.POST.get('residential')
        house_no = request.POST.get('house')
        street = request.POST.get('street')
        block = request.POST.get('block')
        distric= request.POST.get('distric')
        state = request.POST.get('state')
        mobile_no=  request.POST.get('mobile')
        alternate_mobile_no= request.POST.get('mobile_alt')
        email = request.POST.get('email')
        message = request.POST.get('message')
        try :
            data = Distributor_Model.objects.get(distric=distric,status=True)
        except Distributor_Model.DoesNotExist:
            data = None
        if data is not None :
            return JsonResponse({'status':"no",'distric':distric})
        else:
            all_data = Distributor_Model(full_name=full_name,father_name=father_name,date_of_birth=date_of_birth,aadhar_no=aadhar_no,pan_no=pan_no,education=education,occupation=occupation,residential_address=residential_address,house_no=house_no,street=street,block=block,distric=distric,state=state,mobile_no=mobile_no,alternate_mobile_no=alternate_mobile_no,email=email,message=message)
            all_data.save()

            template = render_to_string('email_dist.html',{'name':full_name,'last_name':father_name,'dob':date_of_birth,'aadhar_no':aadhar_no,'pan_no':pan_no,'education':education,'occupation':occupation,'residential':residential_address,'house_no':house_no,'street':street,'block':block,'distric':distric,'state':state,'mobile':mobile_no,'alt_mobile':alternate_mobile_no,'email':email,'message':message})
            template_user = render_to_string('email_user.html')
            email1 = (
            'We got distributor',
            template,
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER],
        )
            
            
            email2 = (
            'Thanks',
            template_user,
            settings.EMAIL_HOST_USER,
            [request.POST.get('email')],
        )
            send_mass_mail((email1,email2),fail_silently=False)
            return JsonResponse({'status':'yes','name':full_name})
     return render(request,'distibutor_page.html')

def investor(request):
    return render(request,'investor2.html')

def test1(request):
    return render(request,'distibutor_page.html')


def user_login(request,user=None):
  if not request.user.is_authenticated:
    if request.method == "POST":
        uname = request.POST['username']
        upass = request.POST['password']
        user = authenticate(username=uname, password=upass)
        if user is not None:
          login(request,user)
          messages.success(request, 'Logged in successfully !!')
          return HttpResponseRedirect('/dashboard/')
        else:
             return render(request, 'login.html',{'d':'yes'})
    else: 

      return render(request, 'login.html')
  else:
    return HttpResponseRedirect('/dashboard/')

# Login View Function

# Logout
def user_logout(request):
  logout(request)
  return redirect('index')

####################      distributor Form View Function         ###################################

@csrf_exempt
def investor_view(request):
    if request.method == "POST":
        full_name = request.POST.get('name')
        company = request.POST.get('company')
        occupation = request.POST.get('occupation')
        aadhar_no= request.POST.get('aadhar')
        residential_address = request.POST.get('residential')
        corresponding_address = request.POST.get('corresponding')
        mobile_no=  request.POST.get('mobile')
        alternate_mobile_no= request.POST.get('mobile_alt')
        email = request.POST.get('email')
        invest= request.POST.get('invest')
        all_data = Investor_Model(full_name=full_name,company=company,occupation=occupation,aadhar_no=aadhar_no,residential_address=residential_address,corresponding_address=corresponding_address,mobile_no=mobile_no,alternate_mobile_no=alternate_mobile_no,email=email,invest_capacity=invest)
        all_data.save()
        ###############email################################
        template = render_to_string('email_investor.html',{'name':full_name,'company':company,'occupation':occupation,'aadhar_no':aadhar_no,'residential_address':residential_address,'corresponding_address':corresponding_address,'mobile_no':mobile_no,'alternate_mobile_no':alternate_mobile_no,'email':email,'invest':invest})
        template_user = render_to_string('email_user.html')
        email1 = (
            'We got a new mail',
            template,
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER],
        )
        
        email2 = (
            'Thanks',
            template_user,
            settings.EMAIL_HOST_USER,
            [request.POST.get('email')],
            
        )
        
        send_mass_mail((email1,email2),fail_silently=False)
        return JsonResponse({"status":"save",'name':full_name})
    else:
        return JsonResponse({"status":"fail"})



####################      End distributor Form View Function         ###################################

####################      Send Mail; View Function         ###################################
@csrf_exempt
def sendmail(request):
    if request.method == "POST":
        name = request.POST['name']
        email_id = request.POST['email']
        mobile = request.POST['mobile']
        message_content  =request.POST['message']
        template = render_to_string('email.html',{'name':name,'email':email_id,'mobile':mobile,'message':message_content})
        email1 = (
            'We got a quary',
            template,
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER],
        )
       
        ################ mail 2  ######################
        email2 =(
            'Thanks for contacting us!',
            "We will contact you soon",
            settings.EMAIL_HOST_USER,
            [request.POST['email']],
            
        )
        
        send_mass_mail((email1,email2),fail_silently=False)
        return JsonResponse({'status':'sent'})
    else:
         return JsonResponse({'status':'not sent'})


    
import json
def getcardata(request):
    if request.method == "GET":
        data = request.GET['id']
        y = json.loads(data)
        card = Add_update.objects.filter(id=y)
        card=list(card)
        
        print("====================================================>",card)
        return JsonResponse({'dt':card})
