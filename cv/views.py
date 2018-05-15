from django.shortcuts import render
from django_filters import rest_framework as filters
from rest_framework import permissions, viewsets

from .models import CV
from .serializers import CVSerializer


class CVViewSet(viewsets.ModelViewSet):
    queryset = CV.objects.all().filter(publish=True)
    serializer_class = CVSerializer
    filter_backends = (filters.DjangoFilterBackend, )
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
