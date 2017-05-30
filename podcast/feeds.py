from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed, Rss201rev2Feed
from django.shortcuts import get_object_or_404
from django.urls import reverse
from datetime import datetime, time
from .models import *
import locale

class iTunesPodcastsFeedGenerator(Rss201rev2Feed):
    def rss_attributes(self):
        return {u"version": self._version,
                u"xmlns:atom": u"http://www.w3.org/2005/Atom",
                u'xmlns:itunes': u'http://www.itunes.com/dtds/podcast-1.0.dtd'}

    def add_root_elements(self, handler):
        super(iTunesPodcastsFeedGenerator, self).add_root_elements(handler)
        handler.addQuickElement(u'pubDate', self.feed['pub_date'])
        handler.addQuickElement(u'itunes:subtitle', self.feed['subtitle'])
        handler.addQuickElement(u'itunes:author', self.feed['author_name'])
        handler.addQuickElement(u'itunes:summary', self.feed['description'])
        handler.addQuickElement(u'itunes:explicit', self.feed['iTunes_explicit'])
        handler.startElement(u"itunes:owner", {})
        handler.addQuickElement(u'itunes:name', self.feed['author_name'])
        handler.addQuickElement(u'itunes:email', self.feed['iTunes_email'])
        handler.endElement(u"itunes:owner")
        handler.startElement(u"image", {})
        handler.addQuickElement(u'url', self.feed['iTunes_image_url'])
        handler.addQuickElement(u'title', self.feed['title'])
        handler.addQuickElement(u'link', self.feed['link'])
        handler.endElement(u"image")
        handler.addQuickElement(u'itunes:image', None,
                                {'href': self.feed['iTunes_image_url']})
        # handler.addQuickElement(u'itunes:keywords', self.feed['iTunes_keywords'])
        handler.startElement(u'itunes:category',
                                {'text': self.feed['parent_category']})
        handler.addQuickElement(u'itunes:category', None,
                                {'text': self.feed['child_category']})
        handler.endElement(u'itunes:category')

    def add_item_elements(self, handler, item):
        super(iTunesPodcastsFeedGenerator, self).add_item_elements(
            handler, item)
        handler.addQuickElement(u'itunes:duration', item['duration'])
        handler.addQuickElement(u'itunes:explicit', item['explicit'])
        handler.addQuickElement(u'itunes:author', item['author'])
        handler.addQuickElement(u'itunes:subtitle', item['subtitle'])
        # handler.startElement(u"image", {})
        # handler.addQuickElement(u'url', item['iTunes_image_url'])
        # handler.addQuickElement(u'title', item['title'])
        # handler.addQuickElement(u'link', item['link'])
        # handler.endElement(u"image")
        handler.addQuickElement(u'itunes:image', None,
                                {'href': item['iTunes_image_url']})
        handler.addQuickElement(u'enclosure', None, 
                                {
                                    'url': item['audio_url'],
                                    'type': item['audio_type'],
                                    'length': item['audio_size'],
                                },
        )

class PodcastFeed(Feed):
    feed_type = iTunesPodcastsFeedGenerator

    iTunes_explicit = u'no'

    def feed_extra_kwargs(self, obj):
        extra_args = {
            'iTunes_email': obj.author_mail,
            'iTunes_explicit': u'no',
            'iTunes_image_url': obj.image.url,
            # 'iTunes_keywords': str(obj.tags),
            'parent_category': obj.parent_category,
            'child_category': obj.child_category,
            'pub_date': datetime.combine(obj.dateCreated, time()).strftime("%Y-%m-%d %H:%M:%S"),
        }

        return extra_args

    def item_extra_kwargs(self, item):
        return {
            'iTunes_image_url': item.image.url,
            'author': item.podcast.author,
            'duration': str(item.duration),
            'explicit': u'no',
            'audio_url': item.audio_mp3.url,
            'audio_type': item.audio_type,
            'audio_size': str(item.audio_size),
            'subtitle': item.small_text,
        }

    def get_object(self, request, podcast_slug):
        return Podcast.objects.get(slug=podcast_slug)

    def title(self, obj):
        return obj.title

    def link(self, obj):
        return obj.get_absolute_url()

    def description(self, obj):
        return obj.text

    # TODO: Override settings language
    def language (self,obj):
        return obj.language

    def author_name(self, obj):
        return obj.author

    def items(self, obj):
        return Episode.objects.filter(podcast=obj)

    def subtitle(self, obj):
        return obj.small_text

    def item_pubdate(self, item):
        return datetime.combine(item.dateCreated, time())

class AtomPodcastFeed(PodcastFeed):
    feed_type = Atom1Feed
    subtitle = PodcastFeed.description

