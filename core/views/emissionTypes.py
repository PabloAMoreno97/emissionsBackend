from rest_framework import viewsets
from core.models import EmissionType
from core.serializers import EmissionTypeSerializer

class EmissionTypeViewSet(viewsets.ModelViewSet):
    queryset = EmissionType.objects.all()
    serializer_class = EmissionTypeSerializer