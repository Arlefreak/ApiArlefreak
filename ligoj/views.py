from django_filters import rest_framework as filters
from rest_framework import permissions, viewsets

from .models import Link, TaggedLink
from .serializers import LinkSerializer, LinkTagSerializer


class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    filter_backends = (filters.DjangoFilterBackend, )
    filter_fields = ('status', )
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )


class LinkTagViewSet(viewsets.ModelViewSet):
    queryset = TaggedLink.objects.all().distinct('tag')
    serializer_class = LinkTagSerializer
    filter_backends = (filters.DjangoFilterBackend, )
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
