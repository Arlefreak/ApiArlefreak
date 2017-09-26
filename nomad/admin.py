from adminsortable.admin import SortableAdmin
from django.contrib import admin
from .models import *

@admin.register(Trip)
class TripAdmin(SortableAdmin):
    list_display = (
        'order',
        'name',
        'color',
    )
    list_display_links = (
        'order',
        'name',
    )
    list_editable = [
        'color',
    ]

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    fieldsets = (
        (None,
            {
                'fields': ('trip',),
            }
         ),
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
        'trip',
    )
    list_display_links = (
        'dateCreated',
        'city',
        'location',
    )
    list_filter = (
        'trip',
    )
    list_editable = [
        'trip',
    ]
