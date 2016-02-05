from .models import Project, ProjectCategory, Link, Image
from .serializers import ProjectSerializer, ProjectCategorySerializer, \
    ProjectLinksSerializer, ImageSerializer
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework import filters


class ProjectViewSet(viewsets.ModelViewSet):
        queryset = Project.objects.all().filter(publish=True)
        serializer_class = ProjectSerializer
        filter_backends = (filters.DjangoFilterBackend,)
        permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ProjectCategoryViewSet(viewsets.ModelViewSet):
        queryset = ProjectCategory.objects.all()
        serializer_class = ProjectCategorySerializer
        filter_backends = (filters.DjangoFilterBackend,)
        permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ProjectLinkViewSet(viewsets.ModelViewSet):
        queryset = Link.objects.all()
        serializer_class = ProjectLinksSerializer
        filter_backends = (filters.DjangoFilterBackend,)
        filter_fields = ('project__id',)
        permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ImageViewSet(viewsets.ModelViewSet):
        queryset = Image.objects.all()
        serializer_class = ImageSerializer
        filter_backends = (filters.DjangoFilterBackend,)
        filter_fields = ('project__id',)
        permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
