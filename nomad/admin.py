from django.contrib import admin
from .models import *

@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'color',
    )

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    fieldsets = (
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
    )
    list_display_links = (
        'dateCreated',
        'city',
        'location',
    )
    # list_editable = [
    #     'title',
    # ]
