from django_filters import rest_framework as filters
from rest_framework import permissions, viewsets

from .models import Image, Post, TaggedPost
from .serializers import ImageSerializer, PostSerializer, PostTagSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().filter(publish=True)
    serializer_class = PostSerializer
    filter_backends = (filters.DjangoFilterBackend, )
    filter_fields = ('tags__name', )
    lookup_field = 'slug'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )


class PostImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    filter_backends = (filters.DjangoFilterBackend, )
    filter_fields = ('post__id', 'imgType')
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )


class PostTagViewSet(viewsets.ModelViewSet):
    queryset = TaggedPost.objects.all().distinct('tag')
    serializer_class = PostTagSerializer
    filter_backends = (filters.DjangoFilterBackend, )
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
