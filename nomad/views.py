from django.shortcuts import render
from .models import City
from .serializers import CitySerializer
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework import filters

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    filter_backends = (filters.DjangoFilterBackend,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
