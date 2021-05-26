from rest_framework import serializers
from .models import TruckOwnerModel,TruckOwnerVehicleRegistraionModel,TruckOwnerDriverRegistration,TransporterModel,TransporterVehicleRegistraionModel,TranspoterDriverRegistration,Tranage_Agent,Tranage_Agent_VehicleRegistraionModel,Tranage_Agent_DriverRegistration


class TrackOwnerSerializer(serializers.Serializer):
    class Meta:
        model  =  TruckOwnerModel
        fields = '__all__'