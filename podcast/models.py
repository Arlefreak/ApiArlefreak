import os
from django.db import models
from django.template.defaultfilters import slugify
from adminsortable.models import SortableMixin
from adminsortable.fields import SortableForeignKey
from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase
from django.urls import reverse

def imageLocation(instance, filename):
    from django.utils.timezone import now
    filename_base, filename_ext = os.path.splitext(filename)
    return 'images/%s%s%s' % (
        filename_base,
        now().strftime("%Y%m%d%H%M%S"),
        filename_ext.lower(),)

def audioLocation(instance, filename):
    from django.utils.timezone import now
    filename_base, filename_ext = os.path.splitext(filename)
    return 'audio/%s%s%s' % (
        filename_base,
        now().strftime("%Y%m%d%H%M%S"),
        filename_ext.lower(),)

class TaggedPodcast(TaggedItemBase):
    content_object = models.ForeignKey('Podcast')

class Podcast(SortableMixin):
    order = models.PositiveIntegerField(default=0, editable=False, db_index=True)
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
    image = models.ImageField(upload_to=imageLocation)
    dateCreated = models.DateField(auto_now_add=True)
    dateUpdated = models.DateField(auto_now=True)
    class Meta:
        ordering = ['order', '-dateCreated']

    def category(self):
        return '%s/%s' % (self.parent_category, self.child_category)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('podcast-feed-rss', args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Podcast, self).save(*args, **kwargs)

class Episode(SortableMixin):
    order = models.PositiveIntegerField(default=0, editable=False, db_index=True)
    podcast = SortableForeignKey(Podcast)
    duration = models.DurationField()
    file_mp3 = models.FileField(upload_to=audioLocation)
    audio_type = models.CharField(max_length=20)
    audio_size = models.CharField(max_length=140)
    title = models.CharField(max_length=140)
    slug = models.SlugField(editable=False)
    text = models.TextField()
    image = models.ImageField(upload_to=imageLocation)
    dateCreated = models.DateField(auto_now_add=True)
    dateUpdated = models.DateField(auto_now=True)
    class Meta:
        ordering = ['order', '-dateCreated']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Episode, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return self.file_mp3.url
