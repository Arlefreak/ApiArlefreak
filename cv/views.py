from django.shortcuts import render
from .models import CV
from .serializers import CVSerializer
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework import filters

class CVViewSet(viewsets.ModelViewSet):
    queryset = CV.objects.all().filter(publish=True)
    serializer_class = CVSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
