

from django.contrib import admin
from django.urls import path,include
from app import views
from dashboard import views as dash
from django.conf.urls.static import static
from django.conf import settings

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
    path('loginn/',views.user_login,name="loginn"),
    # path('add_product/',dash.add_project,name="add_product"),
    path('investor_view/',views.investor_view,name="investor_view")
]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
