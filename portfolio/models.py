from django.db import models
from django.template.defaultfilters import slugify
from adminsortable.models import SortableMixin
from adminsortable.fields import SortableForeignKey
from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase
from embed_video.fields import EmbedVideoField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, Adjust
import os


IMAGE_TYPE = (
    ('mni', 'Main Image'),
    ('gal', 'Gallery'),
)

class TaggedProject(TaggedItemBase):
    content_object = models.ForeignKey('Project')

def imageLocation(instance, filename):
    from django.utils.timezone import now
    filename_base, filename_ext = os.path.splitext(filename)
    return 'images/%s%s%s' % (
        filename_base,
        now().strftime("%Y%m%d%H%M%S"),
        filename_ext.lower(),)


def videoLocation(instance, filename):
    from django.utils.timezone import now
    filename_base, filename_ext = os.path.splitext(filename)
    return 'videos/%s%s%s' % (
        filename_base,
        now().strftime("%Y%m%d%H%M%S"),
        filename_ext.lower(),)

class ProjectCategory(SortableMixin):
    order = models.PositiveIntegerField(default=0, editable=False, db_index=True)
    name = models.CharField(max_length=140)
    slug = models.SlugField(editable=False)
    smallDescription = models.CharField(max_length=140, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(null=True, blank=True)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(ProjectCategory, self).save(*args, **kwargs)

    def image_img(self):
        if self.image:
            return u'<img src="%s" style="width: 100px;'\
                ' height: auto; display: block;"/>' % self.image.url
        else:
            return 'No Image'
    image_img.short_description = 'Image'
    image_img.allow_tags = True

class Project(SortableMixin):
    order = models.PositiveIntegerField(default=0, editable=False, db_index=True)
    publish = models.BooleanField(default=False)
    name = models.CharField(max_length=140)
    slug = models.SlugField(editable=False)
    smallDescription = models.CharField(max_length=140, blank=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey('ProjectCategory')
    tags = TaggableManager(through=TaggedProject)
    date = models.DateField(null=True)
    dateCreated = models.DateField(auto_now_add=True)
    dateUpdated = models.DateField(auto_now=True)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Project, self).save(*args, **kwargs)

    def mainImage(self):
        mainImage = Image.objects.filter(project=self, imgType='mni')[:1].get()
        if mainImage:
            return mainImage.image
        else:
            return 'No Image'

    def gallery(self):
        images = Image.objects.filter(project=self, imgType='gal')
        return images

    def image_img(self):
        mainImage = Image.objects.filter(project=self, imgType='mni')[:1].get()
        if mainImage:
            return u'<img src="%s" style="width: 100px;'\
                ' height: auto; display: block;"/>' % mainImage.image.url
        else:
            return 'No Image'

    def links(self):
        ls = Link.objects.filter(project=self)
        return ls
    image_img.short_description = 'Image'
    image_img.allow_tags = True

class Image(SortableMixin):
    order = models.PositiveIntegerField(default=0, editable=False, db_index=True)
    publish = models.BooleanField(default=False)
    project = models.ForeignKey('Project')
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
        return '%s-%s-%s' % (self.project.slug, self.imgType, self.name)

    def image_img(self):
        if self.image:
            return u'<img src="%s" style="width: 100px;'\
                ' height: auto; display: block;"/>' % self.thumbnail.url
        else:
            return 'No Image'
    image_img.short_description = 'Image'
    image_img.allow_tags = True


class Video(SortableMixin):
    order = models.PositiveIntegerField(default=0, editable=False, db_index=True)
    publish = models.BooleanField(default=False)
    project = SortableForeignKey('Project')
    name = models.CharField(max_length=140)
    caption = models.CharField(max_length=140, blank=True)
    video = EmbedVideoField()
    dateCreated = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'dateCreated']

    def __str__(self):
        return self.name


class Link(SortableMixin):
    order = models.PositiveIntegerField(default=0, editable=False, db_index=True)
    name = models.CharField(max_length=140)
    project = SortableForeignKey('Project')
    link = models.URLField()
    category = models.ForeignKey('LinkCategory')

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return self.name


class LinkCategory(models.Model):
    name = models.CharField(max_length=140)
    slug = models.SlugField(editable=False)
    image = models.FileField(upload_to=imageLocation, null=True, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(LinkCategory, self).save(*args, **kwargs)

    def image_img(self):
        if self.image:
            return u'<img src="%s" style="width: 100px;'\
                ' height: auto; display: block;"/>' % self.image.url
        else:
            return 'No Image'
    image_img.short_description = 'Image'
    image_img.allow_tags = True
