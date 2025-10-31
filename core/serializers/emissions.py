from rest_framework import serializers
from core.models import Emission, Country, Activity, EmissionType
from core.serializers import CountrySerializer, ActivitySerializer, EmissionTypeSerializer


class EmissionSerializer(serializers.ModelSerializer):
    country = serializers.SlugRelatedField(
        slug_field="name", read_only=True
    )
    activity = serializers.SlugRelatedField(
        slug_field="name", read_only=True
    )
    emission_type = serializers.SlugRelatedField(
        slug_field="name", read_only=True
    )
    country_id = serializers.PrimaryKeyRelatedField(
        queryset=Country.objects.all(), write_only=True, source="country"
    )
    activity_id = serializers.PrimaryKeyRelatedField(
        queryset=Activity.objects.all(), write_only=True, source="activity"
    )
    emission_type_id = serializers.PrimaryKeyRelatedField(
        queryset=EmissionType.objects.all(), write_only=True, source="emission_type"
    )

    class Meta:
        model = Emission
        fields = [
            "id",
            "year",
            "emissions",
            "emission_type",
            "country",
            "activity",
            "country_id",
            "activity_id",
            "emission_type_id"
        ]
