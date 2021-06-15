from dashboard.models import Employee_model
from django.shortcuts import render,redirect,HttpResponse
from api.serializers import *
from dashboard.models import Add_project
from  api.models import VehicleRegistraionModel
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
def get_project_by_id(request):
    if request.method =='POST':
        id = request.data.get('id',None)
        if id is not None:
            stu = Add_project.objects.get(id=id)
            serializer = Add_ProjectSerializer(stu)
            return  Response(serializer.data,status=status.HTTP_200_OK)
        else:
            
            return  Response({"status":"Please enter id"},status=status.HTTP_400_OK)
            
class Employee_View(ModelViewSet):
    queryset  = Employee_model.objects.all()
    serializer_class = Employee_modelSerializer
    authetication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

