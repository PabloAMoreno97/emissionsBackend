from django.db import models


class EmissionType(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "EmissionType"
        verbose_name_plural = "EmissionTypes"
        ordering = ["name"]

    def __str__(self):
        return self.name