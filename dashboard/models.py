from django.db import models
from api.models import VehicleRegistraionModel
# Create your models here.
from django.db import models

class Employee_model(models.Model):
    employee_name = models.CharField(max_length=100)
    employee_email = models.CharField(max_length=100)
    employee_mobile = models.CharField(max_length=100)
    user_type = models.CharField(default="employee", max_length=50)
    assigned_project = models.CharField(max_length=100)
    trip_added  = models.CharField(max_length=50,default=0)
    trip_verified = models.CharField(max_length=50,default=0)
    def __str_(self):
        return self.employee_

class Add_update(models.Model):
    heading = models.CharField(max_length=500)
    description = models.CharField(max_length=1000)
    location =  models.CharField(max_length=500)
    expiry_date = models.CharField(max_length=500)



class Add_project(models.Model):

    project_name = models.CharField(max_length=500)
    project_loading_location = models.CharField(max_length=1000)
    project_unloading_location =  models.CharField(max_length=500)
    material_type = models.CharField(max_length=500)
    per_trip_cost = models.CharField(max_length=500)
    per_unit_cost = models.CharField(max_length=500)
    project_start_date = models.CharField(max_length=500)
    project_end_date = models.CharField(max_length=500)
    loading_unit = models.CharField(max_length=500)
    project_loading_employee = models.CharField( max_length=50)
    project_unloading_employee = models.CharField( max_length=50)
    project_status =  models.CharField(max_length=50)
    project_discription = models.TextField()
    mapped_vehicle = models.ManyToManyField(VehicleRegistraionModel, related_name='my_vehicle')
    def get_products(self):
        return ";".join([str(p) for p in self.mapped_vehicle.all()])


class Mapping_model(models.Model):
    vehicle_no = models.CharField(max_length=50)
    project_id = models.CharField( max_length=50)
    Employee_id = models.CharField(max_length=50)