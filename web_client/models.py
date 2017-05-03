import os
from django.db import models
from solo.models import SingletonModel

def imageLocation(instance, filename):
    from django.utils.timezone import now
    filename_base, filename_ext = os.path.splitext(filename)
    return 'images/%s%s%s' % (
        filename_base,
        now().strftime("%Y%m%d%H%M%S"),
        filename_ext.lower(),)

class SiteConfiguration(SingletonModel):
    site_name = models.CharField(max_length=140, default='ellugar.co')
    default_description = models.CharField(max_length=140, default='description')
    default_preview = models.ImageField(upload_to=imageLocation)

    def __str__(self):
        return u"Site Configuration"

    class Meta:
        verbose_name = "Site Configuration"
