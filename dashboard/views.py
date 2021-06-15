from django.shortcuts import render,redirect
from .models import Add_update,Add_project,Employee_model
from app.models import Distributor_Model,Investor_Model
from api.models import *
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='loginn')
def dashboard(request):
    owner = TruckOwnerModel.objects.all()
    transporter = TransporterModel.objects.all()
    return render(request,'dash/index.html',{'owners':owner,'transporters':transporter})

def portfolio(request):
    return render(request,'dash/portofolio.html')

def all_truck_owner(request):
    owner = TruckOwnerModel.objects.all()
    return render(request,'dash/elements/truck_owner_list.html',{'owners':owner})

def all_transpoter_list(request):
    transporter = TransporterModel.objects.all()
    return render(request,'dash/elements/transporter_list.html',{'transporters':transporter})

def all_agent_list(request):
    agent = Tranage_Agent.objects.all()
    return render(request,'dash/elements/agent_list.html',{'agents':agent})

def all_driver_list(request):
    driver = DriverRegistrationModel.objects.all()
    return render(request,'dash/elements/driver_list.html',{'drivers':driver})

def all_vehicle_list(request):
    vehicle = VehicleRegistraionModel.objects.all()
    return render(request,'dash/elements/vehicle_list.html',{'vehicles':vehicle})

def distributor_list(request):
    distributor = Distributor_Model.objects.all()
    return render(request,'dash/elements/distributor_list.html',{'distributors':distributor})

def investor_list(request):
    investor = Investor_Model.objects.all()
    return render(request,'dash/elements/investor_list.html',{'investors':investor})

def recent_update_list(request):
    card = Add_update.objects.all()
    return render(request,'dash/elements/update_list.html',{'cards':card})

def employee_list(request):
    emps = Employee_model.objects.all()
    return render(request,'dash/elements/employee_list.html',{'emps':emps})

def project_list(request):
    project = Add_project.objects.all()
    return render(request,'dash/elements/project_list.html',{'projects':project})

def truck_owner_detail(request,id):
    truck = TruckOwnerModel.objects.get(id=id)
    return render(request,'dash/elements/truck_owner_detail.html',{'truck':truck})

def transporter_detail(request,id):
       
    try:
        truck = TransporterModel.objects.get(id=id)
    except TransporterModel.DoesNotExist:
        truck =None
    return render(request,'dash/elements/transporter_detail.html',{'truck':truck})

def agent_detail(request,id):
       
    try:
        truck = Tranage_Agent.objects.get(id=id)
    except Tranage_Agent.DoesNotExist:
        truck =None
    return render(request,'dash/elements/agent_detail.html',{'truck':truck})    

def add_card(request):
    if request.method =='POST':
        card_data = request.POST
        heading =  card_data.get('heading')
        description =  card_data.get('description')
        location =  card_data.get('location')
        expiry_date =  card_data.get('datepicker')
        all_data = Add_update(heading=heading,description=description,location=location,expiry_date=expiry_date)
        all_data.save()
        return redirect('add_card')
    else :
         return render(request,'dash/elements/add_card.html')

 

from api.models import VehicleRegistraionModel

def add_project(request):
     if request.method == 'POST':
         project_data = request.POST
         project_name=project_data.get('')
         project_loading_location=project_data.get('')
         project_unloading_location=project_data.get('')
         material_type=project_data.get('')
         per_trip_cost=project_data.get('')
         per_unit_cost=project_data.get('')
         project_start_date =project_data.get('')
         project_end_date = project_data.get('')
         loading_unit = project_data.get('')
         project_employee = project_data.get('')
         all_project_data = Add_project()
         all_project_data.save()
         return redirect('project_list')
     else:
         emp = Employee_model.objects.all()
         vehicle = VehicleRegistraionModel.objects.all()
         return render(request,'dash/elements/add_project.html',{"vehicles":vehicle})
    

###################################    ADD EMPLOYEE ################################################
def add_employee(request):
    if request.method =='POST':
        data = request.POST
        employee_name = data.get('employee_name')
        employee_email =  data.get('employee_email')
        employee_mobile =  data.get('employee_mobile')
        assigned_project =  data.get('assigned_project')
        all_data = Employee_model(employee_name=employee_name,employee_email=employee_email,employee_mobile=employee_mobile,assigned_project=assigned_project)
        all_data.save()
        return redirect('add_employee')
    else :
         return render(request,'dash/elements/add_employee.html')
