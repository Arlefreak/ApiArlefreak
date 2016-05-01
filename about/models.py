import os
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, Adjust
from ordered_model.models import OrderedModel
from django.template.defaultfilters import slugify

def imageLocation(instance, filename):
    from django.utils.timezone import now
    filename_base, filename_ext = os.path.splitext(filename)
    return 'images/%s%s%s' % (
        filename_base,
        now().strftime("%Y%m%d%H%M%S"),
        filename_ext.lower(),)

class Entry(OrderedModel):
    publish = models.BooleanField(default=False)
    name = models.CharField(max_length=140)
    slug = models.SlugField(editable=False)
    text = models.TextField()
    dateCreated = models.DateField(auto_now_add=True)
    dateUpdated = models.DateField(auto_now=True)
    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Entry, self).save(*args, **kwargs)

class Image(OrderedModel):
    publish = models.BooleanField(default=False)
    entry = models.ForeignKey('Entry')
    order_with_respect_to = 'entry'
    name = models.CharField(max_length=140)
    caption = models.CharField(max_length=140, blank=True)
    image = models.ImageField(upload_to=imageLocation)
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

