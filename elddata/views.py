from django.shortcuts import render
from django.urls import include, path
from rest_framework import routers

from rest_framework import permissions, viewsets
from .models import EldData
from .serializers import EldDataSerializer

class EldDataViewSet(viewsets.ModelViewSet):
    queryset = EldData.objects.all()
    serializer_class = EldDataSerializer

# Create your views here.
