from django.db import models

from ..models import Country, Activity, EmissionType


class Emission(models.Model):
    year = models.IntegerField()
    emissions = models.FloatField()
    emission_type = models.ForeignKey(EmissionType, on_delete=models.CASCADE, related_name="emissions")
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="emissions")
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name="emissions")

    class Meta:
        ordering = ["-year", "country", "activity"]
        verbose_name = "Emission"
        verbose_name_plural = "Emissions"

    def __str__(self):
        return f"{self.country.name} - {self.emission_type.name} ({self.year})"
    