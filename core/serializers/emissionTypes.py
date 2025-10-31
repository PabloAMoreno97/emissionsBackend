from rest_framework import serializers
from core.models import EmissionType

class EmissionTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = EmissionType
        fields = "__all__"