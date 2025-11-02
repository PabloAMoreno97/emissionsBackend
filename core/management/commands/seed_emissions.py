from django.core.management.base import BaseCommand
from core.models import Emission, Country, Activity, EmissionType
from faker import Faker
import random


class Command(BaseCommand):
    help = "Genearte fake emissions data"

    def handle(self, *args, **kwargs):
        fake = Faker()

        countries = ['USA', 'Colombia', 'Germany', 'Japan', 'Brazil', 'Canada', 'Panama', 'Mexico']
        activities = ['Transport', 'Energy', 'Agriculture', 'Industry', 'Residential']
        emission_types = ['CO2', 'CH4', 'N2O', 'HFC', 'PFC', 'SF6']

        records_to_create = 100

        emissions = []
        country_instances = [Country.objects.get_or_create(name=country) for country in countries]
        activity_instance = [Activity.objects.get_or_create(name=activity) for activity in activities]
        emitssion_types_instance = [EmissionType.objects.get_or_create(name=emission_type) for emission_type in emission_types]


        for _ in range(records_to_create):
            emissions.append(Emission(
                year=random.randint(1990, 2025),
                emissions=round(random.uniform(10,10000), 2),
                emission_type=random.choice(emitssion_types_instance)[0],
                country=random.choice(country_instances)[0],
                activity=random.choice(activity_instance)[0]
            ))

        Emission.objects.bulk_create(emissions)
        self.stdout.write(self.style.SUCCESS(f"Created {records_to_create} fake emissions."))
