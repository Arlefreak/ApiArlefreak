from .models import Podcast, Episode, TaggedPodcast
from .serializers import PodcastSerializer, PodcastTagSerializer, EpisodeSerializer
from rest_framework import permissions
from rest_framework import viewsets, generics
from rest_framework import filters

class PodcastViewSet(viewsets.ModelViewSet):
    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class EpisodeListView(generics.ListAPIView):
    serializer_class = EpisodeSerializer

    def get_queryset(self):
        slug = self.kwargs['podcast_slug']
        return Episode.objects.filter(podcast__slug=slug)


class PodcastTagViewSet(viewsets.ModelViewSet):
    queryset = TaggedPodcast.objects.all().distinct('tag')
    serializer_class = PodcastTagSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
