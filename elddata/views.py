from django.shortcuts import render
from django.urls import include, path
from rest_framework import routers

from rest_framework import permissions, viewsets,views
from rest_framework.response import Response
from .models import EldData, HOSViolation
from .serializers import EldDataSerializer, HOSViolationSerializer
from .utils import detect_hos_violations

class EldDataViewSet(viewsets.ModelViewSet):
    queryset = EldData.objects.all()
    serializer_class = EldDataSerializer

class DetectHOSViolationsView(views.APIView):
    def get(self, request, driver_id):
        violations = detect_hos_violations(driver_id)
        serializer = HOSViolationSerializer(violations, many=True)
        return Response(serializer.data)
# Create your views here.
