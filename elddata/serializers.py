from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import EldData
class EldDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EldData
        #fields = [ 'driverId', 'timestamp', 'location', 'status']
        fields = '__all__'
