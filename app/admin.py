from django.contrib import admin
from app.models import Distributor_Model,Investor_Model
from .models import photos,videos

admin.site.register(photos)
admin.site.register(videos)

@admin.register(Distributor_Model)
class Distributor_admin(admin.ModelAdmin):
    list_display = ['id','full_name']

@admin.register(Investor_Model)
class Investor_admin(admin.ModelAdmin):
    list_display = ['id','full_name']

