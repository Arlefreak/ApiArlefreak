from django.conf.urls import url
from .feeds import *

urlpatterns = [
    url(r'^(?P<podcast_slug>[\w-]+)/rss/$', PodcastFeed(), name='podcast-feed-rss'),
    url(r'^(?P<podcast_slug>[\w-]+)/atom/$', AtomPodcastFeed(), name='podcast-feed-atom'),
]
