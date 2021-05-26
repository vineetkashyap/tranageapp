from api.models import *
from api.serializers import *
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['POST'])
def getdriver(request):
    if request.method =='POST':
        id = request.data.get('id',None)
        if id is not None:
            stu = DriverRegistrationModel.objects.filter(registered_by=id)
            serializer = DriverRegistrationSerializer(stu,many=True)
            return  Response(serializer.data,status=status.HTTP_200_OK)
        else:
            stu =DriverRegistrationModel.objects.all()
            serializer = DriverRegistrationSerializer(stu,many=True)
            return  Response(serializer.data,status=status.HTTP_200_OK)

class DriverRegistrationSerializer_View(ModelViewSet):
    queryset  = DriverRegistrationModel.objects.all()
    serializer_class = DriverRegistrationSerializer
    authetication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]