from django.contrib import admin
from .models import *

# site your models here.
admin.site.register(VehicleRegistraionModel)
admin.site.register(TruckOwnerModel)
admin.site.register(TransporterModel)
admin.site.register(Tranage_Agent)
admin.site.register(Mechanic_model)
admin.site.register(Maintenance_Support)

