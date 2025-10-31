from django.db import models


class Activity(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Activity"
        verbose_name_plural = "Activities"
        ordering = ["name"]

    def __str__(self):
        return self.name