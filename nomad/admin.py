from django.contrib import admin
from .models import *

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    fieldsets = (
        (None,
         {
             'fields': ('title',),
         }),
        ('Dates',
         {
             'fields': ('dateCreated',),
         }),
        ('LOC',
         {
             'fields': ('city', 'location'),
         }),
    )
    list_display = (
        'dateCreated',
        'city',
        'location',
        'title',
    )
    list_display_links = (
        'dateCreated',
        'city',
        'location',
    )
    list_editable = [
        'title',
    ]
