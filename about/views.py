from django.shortcuts import render
from .models import Entry, Image
from .serializers import EntrySerializer, ImageSerializer
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework import filters

class EntryViewSet(viewsets.ModelViewSet):
        queryset = Entry.objects.all().filter(publish=True)
        serializer_class = EntrySerializer
        filter_backends = (filters.DjangoFilterBackend,)
        permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class EntryImageViewSet(viewsets.ModelViewSet):
        queryset = Image.objects.all()
        serializer_class = ImageSerializer
        filter_backends = (filters.DjangoFilterBackend,)
        filter_fields = ('entry__id',)
        permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
