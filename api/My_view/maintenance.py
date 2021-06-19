from api.models import *
from api.serializers import *
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class Maintenance_View(ModelViewSet):
    queryset  = Maintenance_Support.objects.all()
    serializer_class = Maintenance_Serializers
    authetication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]