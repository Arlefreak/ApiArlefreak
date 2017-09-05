from rest_framework import serializers
from .models import City

class CitySerializer(serializers.ModelSerializer):
    coordinates = serializers.SerializerMethodField()
    class Meta:
        fields = (
            'id',
            'dateCreated',
            'title',
            'city',
            'coordinates',
        )
        model = City
    def get_coordinates(self, obj):
        return [float(x.strip()) for x in obj.location.split(',')]
