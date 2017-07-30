from django.db import models
from adminsortable.models import SortableMixin
from django.template.defaultfilters import slugify

class CV(SortableMixin):
    order = models.PositiveIntegerField(default=0, editable=False, db_index=True)
    publish = models.BooleanField(default=False)
    name = models.CharField(max_length=140)
    slug = models.SlugField(editable=False)
    sections = models.ManyToManyField('Section', through='SectionOrder')
    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(CV, self).save(*args, **kwargs)

class Section(models.Model):
    name =  models.CharField(max_length=140)
    slug = models.SlugField(editable=False)
    text = models.TextField()
    class Meta:
        ordering = ['pk', 'name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Section, self).save(*args, **kwargs)

class SectionOrder(models.Model):
    order = models.PositiveIntegerField(default=0, editable=False, db_index=True)
    cv = models.ForeignKey(CV)
    section = models.ForeignKey(Section)
