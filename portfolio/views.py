from .models import Project, ProjectCategory, Link, Image, TaggedProject
from .serializers import ProjectSerializer, ProjectCategorySerializer, \
    ProjectLinksSerializer, ImageSerializer, ProjectTagSerializer
from rest_framework import permissions
from rest_framework import viewsets
from django_filters import rest_framework as filters


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
        filter_fields = ('project__id', 'project__slug')
        permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class ProjectImageViewSet(viewsets.ModelViewSet):
        queryset = Image.objects.all()
        serializer_class = ImageSerializer
        filter_backends = (filters.DjangoFilterBackend,)
        filter_fields = ('project__id', 'project__slug', 'imgType')
        permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
        def filter_queryset(self, queryset):
            queryset = super(ProjectImageViewSet, self).filter_queryset(queryset)
            return queryset.order_by('order')


class ProjectTagViewSet(viewsets.ModelViewSet):
        queryset = TaggedProject.objects.all().distinct('tag')
        serializer_class = ProjectTagSerializer
        filter_backends = (filters.DjangoFilterBackend,)
        permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
