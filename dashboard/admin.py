from django.contrib import admin
from .models import Add_update,Add_project
# Register your models here.

@admin.register(Add_update)
class Add_update_Admin(admin.ModelAdmin):
    list_display = ['id','heading','description','location','expiry_date']

@admin.register(Add_project)
class Add_project_Admin(admin.ModelAdmin):
    list_display = ['id','project_name','project_loading_location','project_unloading_location','material_type','per_trip_cost','per_unit_cost','project_start_date','project_end_date','loading_unit','project_employee','get_products']

