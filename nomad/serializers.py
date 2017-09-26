from rest_framework import serializers
from .models import Trip, City

class CitySerializer(serializers.ModelSerializer):
    coordinates = serializers.SerializerMethodField()
    class Meta:
        fields = (
            'id',
            'dateCreated',
            'city',
            'coordinates',
        )
        model = City
    def get_coordinates(self, obj):
        return [float(x.strip()) for x in obj.location.split(',')]

class TripSerializer(serializers.ModelSerializer):
    cities = CitySerializer(many=True, read_only=True)
    # serializers.StringRelatedField(many=True)
    class Meta:
        fields = (
            'id',
            'name',
            'color',
            'cities',
        )
        model = Trip
