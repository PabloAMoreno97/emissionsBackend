import django_filters
from ..models import Emission

class EmissionFilter(django_filters.FilterSet):
    country = django_filters.CharFilter(field_name='country__name', lookup_expr='icontains')
    activity = django_filters.CharFilter(field_name='activity__name', lookup_expr='icontains')
    emission_type = django_filters.CharFilter(field_name='emission_type__name', lookup_expr='icontains')

    class Meta:
        model = Emission
        fields = ['country', 'activity', 'emission_type']