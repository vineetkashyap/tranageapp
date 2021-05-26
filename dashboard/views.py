from django.shortcuts import render,redirect
from .models import Add_update,Add_project
from api.models import *
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='loginn')
def dashboard(request):
    return render(request,'dash/index.html')

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

def add_card(request):
    if request.method =='POST':
        card_data = request.POST
        heading =  card_data.get('heading')
        description =  card_data.get('description')
        location =  card_data.get('location')
        expiry_date =  card_data.get('datepicker')
        all_data = Add_update(heading=heading,description=description,location=location,expiry_date=expiry_date)
        all_data.save()
        return redirect('index')
    else :
         return render(request,'dash/elements/add_card.html')

 

   

# def add_project(request):
#     if request.method == 'POST':
#         project_data = request.POST
#         project_name=project_data.get('')
#         project_loading_location=project_data.get('')
#         project_unloading_location=project_data.get('')
#         material_type=project_data.get('')
#         per_trip_cost=project_data.get('')
#         per_unit_cost=project_data.get('')
#         project_start_date =project_data.get('')
#         project_end_date = project_data.get('')
#         loading_unit = project_data.get('')
#         project_employee = project_data.get('')
#         all_project_data = Add_project()
#         all_project_data.save()
#         return redirect('project_list')
#     else:
#         return render(request,'dash/elements/add_project.html')
    

