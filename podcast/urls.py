from django.conf.urls import url, include
from .feeds import *
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'podcast', PodcastViewSet)
router.register(r'podcastTags', PodcastTagViewSet)

urlpatterns = [
    url(r'^(?P<podcast_slug>[\w-]+)/rss/$', PodcastFeed(), name='podcast-feed-rss'),
    url(r'^(?P<podcast_slug>[\w-]+)/atom/$', AtomPodcastFeed(), name='podcast-feed-atom'),
    url(r'^json/', include(router.urls)),
    url('^json/episodes/(?P<podcast_slug>[\w-]+)/$', EpisodeListView.as_view()),
]
