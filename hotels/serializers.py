from .models import Hotel, City
from rest_framework import serializers


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name']


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['id', 'name', 'address', 'contact_email', 'contact_phone', 'city']

    class JSONAPIMeta:
        included_resources = ['city']

    included_serializers = {
        'city': CitySerializer,
    }


