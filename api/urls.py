from django.contrib import admin
from django.urls import path,include
from api import views
from api.My_view import truck_owner,agent,driver,transporter,vehicle,add_project,employee_detail,loading
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.authtoken.views import obtain_auth_token
from knox import views as knox_views
from rest_framework.routers import DefaultRouter
router= DefaultRouter()
router.register('truckowner',truck_owner.TruckOwnerModel_View,basename='truckowner')
router.register('transporter',transporter.TransporterModel_View,basename='transporter')
router.register('agent',agent.Tranage_AgentSerializer_View,basename='agent')
router.register('vehicle',vehicle.VehicleRegistraionModelSerializer_View,basename='vehicle')
router.register('driver',driver.DriverRegistrationSerializer_View,basename='driver')
router.register('add_project',add_project.AddProject_View,basename='add_project')
router.register('getemp',employee_detail.Employee_View,basename='getemp')
router.register('loading',loading.Loading_View,basename='loading')


urlpatterns = [
    
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls')),
    path('gettoken/',obtain_auth_token),
    path('gettruckowner/',truck_owner.gettruckowner,name='gettruckowner'),
    path('gettransporter/',transporter.gettransporter,name='gettransporter'),
    path('getagent/',agent.getagent,name='getagent'),

    path('getdriver/',driver.getdriver,name='getdriver'),
    path('getvehicle/',vehicle.getvehicle,name='getvehicle'),

    path('api/register/', views.RegisterAPI.as_view(), name='register'),
    path('api/login/', views.LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),

    path('getpro/',add_project.all_service_json,name='all_service_json'),
    path('getprod/',add_project.getprod,name='all_service_jsond'),

    path('get_project_by_id/',employee_detail.get_project_by_id,name='get_project_by_id'),




]