from django.db import models
from adminsortable.models import SortableMixin
from django.template.defaultfilters import slugify
from location_field.models.plain import PlainLocationField
from colorful.fields import RGBColorField

class Trip(SortableMixin):
    order = models.PositiveIntegerField(default=0, editable=False, db_index=True)
    name = models.CharField(max_length=140, null=True, blank=True)
    slug = models.SlugField(editable=False)
    color = RGBColorField(default="#ffffff")
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Trip, self).save(*args, **kwargs)

    class Meta:
        ordering = ['order', 'slug']

    def __str__(self):
        return '%s - %s' % (self.name, self.color)

class City(models.Model):
    city = models.CharField(max_length=255)
    trip = models.ForeignKey('Trip', related_name='cities')
    location = PlainLocationField(based_fields=['city'], zoom=7)
    dateCreated = models.DateField()
    class Meta:
        ordering = ['-dateCreated',]

    def __str__(self):
        return self.city
