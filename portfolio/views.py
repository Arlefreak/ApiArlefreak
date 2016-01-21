from .models import Project
from .serializers import ProjectSerializer
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework import filters


class ProjectViewSet(viewsets.ModelViewSet):
        queryset = Project.objects.all()
        serializer_class = ProjectSerializer
        filter_backends = (filters.DjangoFilterBackend,)
        # filter_fields = ('slug', 'price', 'publish')
        permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
