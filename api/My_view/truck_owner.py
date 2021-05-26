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
def gettruckowner(request):
    if request.method =='POST':
        id = request.data.get('id',None)
        if id is not None:
            stu = TruckOwnerModel.objects.get(email_id=id)
            serializer = TruckOwnerModelSerializer(stu)
            return  Response(serializer.data,status=status.HTTP_200_OK)
        else:
            stu =TruckOwnerModel.objects.all()
            serializer = TruckOwnerModelSerializer(stu,many=True)
            return  Response(serializer.data,status=status.HTTP_200_OK)

class TruckOwnerModel_View(ModelViewSet):
    queryset  = TruckOwnerModel.objects.all()
    serializer_class = TruckOwnerModelSerializer
    authetication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]