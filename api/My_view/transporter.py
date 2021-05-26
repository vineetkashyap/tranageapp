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
def gettransporter(request):
    if request.method =='POST':
        id = request.data.get('id',None)
        if id is not None:
            stu = TransporterModel.objects.get(email=id)
            serializer = TransporterModelSerializer(stu)
            return  Response(serializer.data,status=status.HTTP_200_OK)
        else:
            stu =TransporterModel.objects.all()
            serializer = TransporterModelSerializer(stu,many=True)
            return  Response(serializer.data,status=status.HTTP_200_OK)
    # else :
    #     res = {'msg':'Oooh GOD'}
    #     return  Response(res,status=status.HTTP_200_OK)
class TransporterModel_View(ModelViewSet):
    queryset  = TransporterModel.objects.all()
    serializer_class = TransporterModelSerializer
    authetication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]