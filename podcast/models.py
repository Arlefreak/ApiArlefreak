import os.path

import html2text
import misaka as m
from adminsortable.fields import SortableForeignKey
from adminsortable.models import SortableMixin
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase

htmlConverter = html2text.HTML2Text()
htmlConverter.ignore_links = True
htmlConverter.ignore_images = True
htmlConverter.ul_item_mark = '-'
htmlConverter.inline_links = False
htmlConverter.ignore_emphasis = True


def imageLocation(instance, filename):
    return 'image/'


def audioLocation(instance, filename):
    return 'audio/'


def upload_to_podcast_cover(instance, filename):
    filename_base, filename_ext = os.path.splitext(filename)
    return 'podcast/covers/%s%s' % (
        instance.slug,
        filename_ext.lower(),
    )


def upload_to_episode_cover(instance, filename):
    filename_base, filename_ext = os.path.splitext(filename)
    return 'podcast/episodes/covers/%s%s' % (
        instance.slug,
        filename_ext.lower(),
    )


def upload_to_episode_audio(instance, filename):
    filename_base, filename_ext = os.path.splitext(filename)
    return 'podcast/episodes/audios/%s%s' % (
        instance.slug,
        filename_ext.lower(),
    )


class TaggedPodcast(TaggedItemBase):
    content_object = models.ForeignKey('Podcast', on_delete=models.CASCADE)


class Podcast(SortableMixin):
    order = models.PositiveIntegerField(
        default=0, editable=False, db_index=True)
    title = models.CharField(max_length=140)
    author = models.CharField(max_length=140)
    author_mail = models.EmailField(max_length=140)
    slug = models.SlugField(editable=False)
    text = models.TextField()
    small_text = models.CharField(max_length=255)
    parent_category = models.CharField(max_length=140)
    child_category = models.CharField(max_length=140)
    language = models.CharField(max_length=10)
    tags = TaggableManager(through=TaggedPodcast, blank=True)
    image = models.ImageField(upload_to=upload_to_podcast_cover)
    website = models.URLField()
    episodesUrl = models.URLField()
    iTunesURL = models.URLField(blank=True, null=True)
    feedBurner = models.URLField(blank=True, null=True)
    dateCreated = models.DateField(auto_now_add=True)
    dateUpdated = models.DateField(auto_now=True)

    class Meta:
        ordering = ['order', '-dateCreated']

    def plain_text(self):
        html_text = m.html(self.text)
        plain = htmlConverter.handle(html_text)
        return plain

    def encoded_text(self):
        html_text = m.html(self.text)
        return html_text

    def feed(self):
        if (self.feedBurner):
            return self.feedBurner
        else:
            return 'https://api.ellugar.co%s' % reverse(
                'podcast-feed-rss', kwargs={'podcast_slug': self.slug})

    def category(self):
        return '%s/%s' % (self.parent_category, self.child_category)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return self.website

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        if self.pk is None:
            saved_image = self.image
            super(Podcast, self).save(*args, **kwargs)
            self.image = saved_image

        super(Podcast, self).save(*args, **kwargs)


class Episode(SortableMixin):
    order = models.PositiveIntegerField(
        default=0, editable=False, db_index=True)
    podcast = SortableForeignKey(Podcast, on_delete=models.CASCADE)
    duration = models.DurationField()
    audio_mp3 = models.FileField(upload_to=upload_to_episode_audio)
    audio_ogg = models.FileField(upload_to=upload_to_episode_audio, blank=True)
    audio_type = models.CharField(max_length=20)
    audio_size = models.PositiveIntegerField(default=1)
    title = models.CharField(max_length=140)
    slug = models.SlugField(editable=False)
    text = models.TextField()
    small_text = models.CharField(max_length=255)
    image = models.ImageField(upload_to=upload_to_episode_cover)
    dateCreated = models.DateField(auto_now_add=True)
    dateUpdated = models.DateField(auto_now=True)

    class Meta:
        ordering = ['order', '-dateCreated']

    def __str__(self):
        return self.title

    def plain_text(self):
        html_text = m.html(self.text)
        plain = htmlConverter.handle(html_text)
        return plain

    def encoded_text(self):
        html_text = m.html(self.text)
        return html_text

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        if self.pk is None:
            saved_audio_mp3 = self.audio_mp3
            saved_audio_ogg = self.audio_ogg
            saved_image = self.image

            self.audio_mp3 = None
            self.audio_ogg = None
            self.image = None

            super(Episode, self).save(*args, **kwargs)

            self.audio_mp3 = saved_audio_mp3
            self.audio_ogg = saved_audio_ogg
            self.image = saved_image

        super(Episode, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return '%s/%s' % (self.podcast.episodesUrl, self.slug)
