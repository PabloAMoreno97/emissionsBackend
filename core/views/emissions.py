from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from core.models import Emission
from core.filters import EmissionFilter
from core.serializers import EmissionSerializer

class EmissionViewSet(viewsets.ModelViewSet):
    queryset = Emission.objects.all()
    serializer_class = EmissionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = EmissionFilter
    ordering_fields = ["year", "emissions"]
    ordering = ["-year"]