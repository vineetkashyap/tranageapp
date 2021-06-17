from django.shortcuts import render
from dashboard.models import Add_update,Add_project
from .serializers import Add_Card_Serializers,Get_project
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

##########LOGIN#####################
from django.contrib.auth import login

from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)

@api_view(['GET'])
def recent_card_api(request):
    
        stu =Add_update.objects.all()
        serializer = Add_Card_Serializers(stu,many=True)
        return  Response(serializer.data,status=status.HTTP_200_OK)


@api_view(['POST'])
def get_project_by_id(request):
    
        stu =Add_project.objects.filter(id=id)
        serializer = Get_project(stu,many=True)
        return  Response(serializer.data,status=status.HTTP_200_OK)

##########LOGIN END#####################
