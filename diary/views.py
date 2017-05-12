from .models import Post, Image, TaggedPost
from .serializers import PostSerializer, ImageSerializer, PostTagSerializer
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework import filters


class PostViewSet(viewsets.ModelViewSet):
        queryset = Post.objects.all().filter(publish=True)
        serializer_class = PostSerializer
        filter_backends = (filters.DjangoFilterBackend,)
        permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class PostImageViewSet(viewsets.ModelViewSet):
        queryset = Image.objects.all()
        serializer_class = ImageSerializer
        filter_backends = (filters.DjangoFilterBackend,)
        filter_fields = ('post__id','imgType')
        permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class PostTagViewSet(viewsets.ModelViewSet):
        queryset = TaggedPost.objects.all().distinct('tag')
        serializer_class = PostTagSerializer
        filter_backends = (filters.DjangoFilterBackend,)
        permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
