from django.shortcuts import render
from .models import City, Trip
from .serializers import CitySerializer, TripSerializer
from rest_framework import permissions
from rest_framework import viewsets
from django_filters import rest_framework as filters

class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    filter_backends = (filters.DjangoFilterBackend,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
