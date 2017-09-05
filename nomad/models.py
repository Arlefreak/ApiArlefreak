from django.db import models
from location_field.models.plain import PlainLocationField

class City(models.Model):
    title = models.CharField(max_length=140, null=True, blank=True)
    city = models.CharField(max_length=255)
    location = PlainLocationField(based_fields=['city'], zoom=7)
    dateCreated = models.DateField()
    class Meta:
        ordering = ['-dateCreated',]

    def __str__(self):
        return self.city
