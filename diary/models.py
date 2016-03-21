from django.db import models
from django.template.defaultfilters import slugify
from ordered_model.models import OrderedModel
from taggit.managers import TaggableManager
from embed_video.fields import EmbedVideoField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, Adjust
import os

IMAGE_TYPE = (
    ('mni', 'Main Image'),
    ('gal', 'Gallery'),
)

def imageLocation(instance, filename):
    from django.utils.timezone import now
    filename_base, filename_ext = os.path.splitext(filename)
    return 'images/%s%s%s' % (
        filename_base,
        now().strftime("%Y%m%d%H%M%S"),
        filename_ext.lower(),)


class Post(OrderedModel):
    publish = models.BooleanField(default=False)
    title = models.CharField(max_length=140)
    slug = models.SlugField(editable=False)
    text = models.TextField()
    tags = TaggableManager(blank=True)
    dateCreated = models.DateField(auto_now_add=True)
    dateUpdated = models.DateField(auto_now=True)
    class Meta:
        ordering = ['-dateCreated', 'order', 'title']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def mainImage(self):
        mainImage = Image.objects.filter(post=self, imgType='mni')[:1].get()
        if mainImage:
            return mainImage.image
        else:
            return 'No Image'

    def gallery(self):
        images = Image.objects.filter(post=self, imgType='gal')
        return images

    def image_img(self):
        mainImage = Image.objects.filter(post=self, imgType='mni')[:1].get()
        if mainImage:
            return u'<img src="%s" style="width: 100px;'\
                ' height: auto; display: block;"/>' % mainImage.image.url
        else:
            return 'No Image'

    image_img.short_description = 'Image'
    image_img.allow_tags = True


class Image(OrderedModel):
    publish = models.BooleanField(default=False)
    post = models.ForeignKey('Post')
    order_with_respect_to = 'post'
    name = models.CharField(max_length=140)
    caption = models.CharField(max_length=140, blank=True)
    image = models.ImageField(upload_to=imageLocation)
    imgType = models.CharField(max_length=3, choices=IMAGE_TYPE, default='gal')
    dateCreated = models.DateField(auto_now_add=True)
    thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(200, 200)],
        format='PNG',
        options={'quality': 100})
    thumbnailBW = ImageSpecField(
        source='image',
        processors=[Adjust(color=0.0),ResizeToFill(200, 200)],
        format='PNG',
        options={'quality': 100})

    class Meta:
        ordering = ['order', 'dateCreated']

    def __str__(self):
        return self.name

    def image_img(self):
        if self.image:
            return u'<img src="%s" style="width: 100px;'\
                ' height: auto; display: block;"/>' % self.thumbnail.url
        else:
            return 'No Image'
    image_img.short_description = 'Image'
    image_img.allow_tags = True


class Video(OrderedModel):
    publish = models.BooleanField(default=False)
    post = models.ForeignKey('Post')
    order_with_respect_to = 'Post'
    name = models.CharField(max_length=140)
    caption = models.CharField(max_length=140, blank=True)
    video = EmbedVideoField()
    dateCreated = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'dateCreated']

    def __str__(self):
        return self.name
