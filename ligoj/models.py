from __future__ import unicode_literals

from django.db import models
import tldextract
from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase
from urllib import request
from bs4 import BeautifulSoup

ACTIVE = 'ACT'
HIDDEN = 'HID'
STATUS = (
    (ACTIVE, 'active'),
    (HIDDEN, 'hidden'),
)

class TaggedLink(TaggedItemBase):
    content_object = models.ForeignKey('Link')

class Link(models.Model):
    link = models.URLField()
    name = models.CharField(editable=False, max_length=140, default="no name")
    status = models.CharField(
        max_length=3,
        choices=STATUS,
        default=ACTIVE
    )
    tags = TaggableManager(through=TaggedLink, blank=True)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    class Meta:
        ordering = ['-date_created']
    def domain(self):
        domain = ""
        name = "no domain"
        if tldextract.extract(self.link).registered_domain:
            domain = tldextract.extract(self.link).registered_domain 
        if(domain):
            name = "%s" % (domain)
        return name
    def save(self, *args, **kwargs):
        try:
            req = request.Request(self.link, headers={'User-Agent' : "Magic Browser"}) 
            con = request.urlopen( req )
            soup = BeautifulSoup(con, "html.parser")
            if(soup.title.string):
                self.name= soup.title.string
        except:
            self.name = self.domain()
        super(Link, self).save(*args, **kwargs)
    def __str__(self):
        return self.name
