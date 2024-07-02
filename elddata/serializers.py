from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import EldData, HOSViolation
class EldDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EldData
        #fields = [ 'driverId', 'timestamp', 'location', 'status']
        fields = '__all__'

class HOSViolationSerializer(serializers.ModelSerializer):
    class Meta:
        model = HOSViolation
        fields = '__all__'
