from django.contrib import admin
from .models import Emission, Country, Activity, EmissionType

admin.site.register(Emission)
admin.site.register(Country)
admin.site.register(Activity)
admin.site.register(EmissionType)