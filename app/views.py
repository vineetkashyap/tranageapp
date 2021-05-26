from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from dashboard.models import Add_update
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

def  login(request):
    return render(request,'login.html')

def registration(request):
    return render(request,'registrationform.html')


def product(request):
    return render(request,'tproduct.html')

def distributor(request):
    return render(request,'contact2.html')

def investor(request):
    return render(request,'investor.html')
















from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

# Signup View Function
# def sign_up(request):
#  if request.method == "POST":
#   fm = SignUpForm(request.POST)
#   if fm.is_valid():
#    messages.success(request, 'Account Created Successfully !!') 
#    fm.save()
#  else: 
#   fm = SignUpForm()
#  return render(request, 'enroll/signup.html', {'form':fm})

# Login View Function
def user_login(request):
  if not request.user.is_authenticated:
    if request.method == "POST":
        uname = request.POST.get('username')
        upass =  request.POST.get('password')
        user = authenticate(username=uname, password=upass)
        if user is not None:
          login(request, user)
          messages.success(request, 'Logged in successfully !!')
          return HttpResponseRedirect('/dashboard/')
        else:
             return render(request, 'login.html')
    else: 
        return render(request, 'login.html')
      
    
  else:
    return HttpResponseRedirect('/dashboard/')


# def user_login(request):
#   if not request.user.is_authenticated:
#     if request.method == "POST":
#       fm = AuthenticationForm(request=request, data=request.POST)
#       if fm.is_valid():
#         uname = fm.cleaned_data['username']
#         upass = fm.cleaned_data['password']
#         user = authenticate(username=uname, password=upass)
#         if user is not None:
#           login(request, user)
#           messages.success(request, 'Logged in successfully !!')
#           return HttpResponseRedirect('/dashboard/')
#     else: 
#       fm = AuthenticationForm()
#     return render(request, 'login.html', {'form':fm})
#   else:
#     return HttpResponseRedirect('/dashboard/')