from rest_framework.test import APITestCase
from rest_framework import status
from core.models import Emission, Country, Activity, EmissionType


class EmissionAPITest(APITestCase):
    def setUp(self):
        self.emissions_endpoint = "/api/emissions/"

        self.country1 = Country.objects.create(name="TestCountry1")
        self.activity1 = Activity.objects.create(name="TestActivity1")
        self.emission_type1 = EmissionType.objects.create(name="TestEmissionType1")

        self.emission1 = Emission.objects.create(
            year=2024,
            emissions=123.45,
            emission_type=self.emission_type1,
            country=self.country1,
            activity=self.activity1,
        )

        self.country2 = Country.objects.create(name="TestCountry2")
        self.activity2 = Activity.objects.create(name="TestActivity2")
        self.emission_type2 = EmissionType.objects.create(name="TestEmissionType2")

        self.emission2 = Emission.objects.create(
            year=2025,
            emissions=543.34,
            emission_type=self.emission_type2,
            country=self.country2,
            activity=self.activity2,
        )


    def test_emission_list_returns_correct_data(self):

        response = self.client.get(self.emissions_endpoint)

        emission_data = list(filter(lambda emission: emission['id']==self.emission2.id, response.data))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(len(emission_data), 1)

        emission_data = emission_data[0]

        self.assertEqual(emission_data["year"], 2025)
        self.assertEqual(emission_data["emissions"], 543.34)
        self.assertEqual(emission_data["country"], self.country2.name)
        self.assertEqual(emission_data["activity"], self.activity2.name)
        self.assertEqual(emission_data["emission_type"], self.emission_type2.name)

    def test_emission_get_returns_correct_data(self):
        url = f"{self.emissions_endpoint}{self.emission1.id}/"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        emission_data = response.data

        self.assertEqual(emission_data["year"], 2024)
        self.assertEqual(emission_data["emissions"], 123.45)
        self.assertEqual(emission_data["country"], self.country1.name)
        self.assertEqual(emission_data["activity"], self.activity1.name)
        self.assertEqual(emission_data["emission_type"], self.emission_type1.name)
    
    def test_emission_delete(self):
        url = f"{self.emissions_endpoint}{self.emission1.id}/"
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Emission.objects.filter(id=self.emission1.id).exists())

    def test_patch_emission(self):
        url = f"{self.emissions_endpoint}{self.emission2.id}/"
        data = {"emissions": 200.5}

        response = self.client.patch(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.emission2.refresh_from_db()
        self.assertEqual(self.emission2.emissions, 200.5)

    def test_post_emission(self):
        data = {
            "emissions": 100,
            "year": 2023,
            "country_id": self.country1.id,
            "activity_id": self.activity2.id,
            "emission_type_id": self.emission_type1.id
        }
        response = self.client.post(self.emissions_endpoint, data, format="json")
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        new_emission_id = response.data["id"]

        get_url = f"{self.emissions_endpoint}{new_emission_id}/"
        get_response = self.client.get(get_url)

        self.assertEqual(get_response.status_code, status.HTTP_200_OK)
        self.assertEqual(get_response.data["id"], new_emission_id)


    def test_put_emission(self):
        url = f"{self.emissions_endpoint}{self.emission2.id}/"
        data = {
            "emissions": 20,
            "year": 2020,
            "country_id": self.country2.id,
            "activity_id": self.activity1.id,
            "emission_type_id": self.emission_type1.id
        }

        response = self.client.put(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.emission2.refresh_from_db()
        self.assertEqual(self.emission2.emissions, 20)
        self.assertEqual(self.emission2.emission_type, self.emission_type1)