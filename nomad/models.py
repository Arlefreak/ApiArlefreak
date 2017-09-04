from django.db import models
from location_field.models.plain import PlainLocationField

class City(models.Model):
    title = models.CharField(max_length=140, null=True, blank=True)
    city = models.CharField(max_length=255)
    location = PlainLocationField(based_fields=['city'], zoom=7)
    date_init = models.DateField()
    date_final = models.DateField()
    class Meta:
        ordering = ['-date_final',]

    def __str__(self):
        return self.city
