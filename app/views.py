from django import template
from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from dashboard.models import Add_update
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, logout,login
from app.models import Distributor_Model,Investor_Model

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

# def  login(request):
#     return render(request,'login.html')

def registration(request):
    return render(request,'registrationform.html')


def product(request):
    return render(request,'productpage.html')

def distributor(request):
     if request.method == "POST":
        full_name = request.POST.get('name')
        father_name = request.POST.get('fathername')
        date_of_birth = request.POST.get('dob')
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
            data = Distributor_Model.objects.get(distric=distric)
        except Distributor_Model.DoesNotExist:
            data = None
        if data is not None :
            messages.success(request, 'Region Not Available')
        else:
            all_data = Distributor_Model(full_name=full_name,father_name=father_name,date_of_birth=date_of_birth,aadhar_no=aadhar_no,pan_no=pan_no,education=education,occupation=occupation,residential_address=residential_address,house_no=house_no,street=street,block=block,distric=distric,state=state,mobile_no=mobile_no,alternate_mobile_no=alternate_mobile_no,email=email,message=message)
            all_data.save()
            return render(request,'distributor_success.html')
     return render(request,'con.html')

def investor(request):
    return render(request,'investor2.html')

def test1(request):
    return render(request,'con.html')







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
      return render(request, 'login.html')
  else:
    return HttpResponseRedirect('/dashboard/')

# Login View Function

# Logout
def user_logout(request):
  logout(request)
  return redirect('index')

####################      distributor Form View Function         ###################################

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
        return render(request,'investor_success.html')


####################      End distributor Form View Function         ###################################



####################      Send Mail; View Function         ###################################
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
def sendmail(request):
    name = request.POST['name']
    email_id = request.POST['email']
    mobile = request.POST['mobile']
    message_content  =request.POST['message']
    template = render_to_string('email.html',{'name':name,'email':email_id,'mobile':mobile,'message':message_content})
    email = EmailMessage(
        'Hello Priye Grahak',
        template,
        settings.EMAIL_HOST_USER,
        [settings.EMAIL_HOST_USER],
    )
    email.fail_silently=False
    email.send()
    return render(request,'email_success.html')