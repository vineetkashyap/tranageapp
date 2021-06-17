

from django.contrib import admin
from django.urls import path,include
from app import views
from app.utils import send_email_otp,send_mobile_otp
from dashboard import views as dash
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('api.urls')),
    # path('dash/',include('dashboard.urls')),
    path('',views.index,name="index"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('team/',views.team,name="team"),
    path('service/',views.service,name="service"),
    path('partner/',views.partner,name="partner"),
    path('blog/',views.blog,name="blog"),
    path('login/',views.login,name="login"),
    path('registration/',views.registration,name="registration"),
    path('product/',views.product,name="product"),
    path('distributor/',views.distributor,name="distributor"),
    path('investor/',views.investor,name="investor"),
    path('dashboard/',dash.dashboard,name="dashboard"),
    path('portfolio/',dash.portfolio,name="portfolio"),
    path('truckowner/',dash.all_truck_owner,name="truckowner"),
    path('all_transpoter_list/',dash.all_transpoter_list,name="all_transpoter_list"),
    path('all_agent_list/',dash.all_agent_list,name="all_agent_list"),
    path('all_driver_list/',dash.all_driver_list,name="all_driver_list"),
    path('all_vehicle_list/',dash.all_vehicle_list,name="all_vehicle_list"),
    path('distributor_list/',dash.distributor_list,name="distributor_list"),
    path('investor_list/',dash.investor_list,name="investor_list"),
    path('add_card/',dash.add_card,name="add_card"),
    path('user_login/',views.user_login,name="user_login"),
    path('user_logout/',views.user_logout,name="user_logout"),
    path('add_project/',dash.add_project,name="add_project"),
    path('investor_view/',views.investor_view,name="investor_view"),
    path('recent_update_list/',dash.recent_update_list,name="recent_update_list"),
    path('employee_list/',dash.employee_list,name="employee_list"),
    path('project_list/',dash.project_list,name="project_list"),
    path('truck_owner_detail/<int:id>',dash.truck_owner_detail,name="truck_owner_detail"),
    path('transporter_detail/<int:id>',dash.transporter_detail,name="transporter_detail"),
    path('agent_detail/<int:id>',dash.agent_detail,name="agent_detail"),
    path('driver_detail/<int:id>',dash.driver_detail,name="driver_detail"),
    path('add_employee/',dash.add_employee,name="add_employee"),
    path('sendmail/',views.sendmail,name="sendmail"),
    path('getcardata/',views.getcardata,name="getcardata"),
    path('enquiry/',views.enquiry,name="enquiry"),
    path('trip_List/',dash.trip_List,name="trip_List"),

    path('con/',views.test1,name='con')
]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

handler404 = 'app.views.error404'