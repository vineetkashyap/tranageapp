from django.contrib import admin
from app.models import Distributor_Model,Investor_Model

@admin.register(Distributor_Model)
class Distributor_admin(admin.ModelAdmin):
    list_display = ['id','full_name']

@admin.register(Investor_Model)
class Investor_admin(admin.ModelAdmin):
    list_display = ['id','full_name']