from dashboard.models import Add_project
from django.shortcuts import render,redirect,HttpResponse
from api.serializers import *
from  api.models import VehicleRegistraionModel
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# @api_view(['POST'])
# def getagent(request):
#     if request.method =='POST':
#         id = request.data.get('id',None)
#         if id is not None:
#             stu = Tranage_Agent.objects.get(email_id=id)
#             serializer = Tranage_AgentSerializer(stu)
#             return  Response(serializer.data,status=status.HTTP_200_OK)
#         else:
#             stu =Tranage_Agent.objects.all()
#             serializer = Tranage_AgentSerializer(stu,many=True)
#             return  Response(serializer.data,status=status.HTTP_200_OK)
            
class AddProject_View(ModelViewSet):
    queryset  = Add_project.objects.all()
    serializer_class = Add_ProjectSerializer
    authetication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

def all_service_json(request):
    services = Add_project.objects.all()
    data = Add_ProjectSerializer(services, many=True).data
    return HttpResponse(data)

@api_view(['POST'])
def getprod(request):
    if request.method =='POST':
        id = request.data.get('id',None)
        if id is not None:
            stu = Add_project.objects.get(mapped_vehicle__vehicle_registration_number=id)
            serializer = Add_ProjectSerializer(stu)
            return  Response(serializer.data,status=status.HTTP_200_OK)
        else:
            stu =Add_project.objects.all()
            serializer = Add_ProjectSerializer(stu,many=True)
            return  Response(serializer.data,status=status.HTTP_200_OK)
            