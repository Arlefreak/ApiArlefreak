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
             'fields': ('date_init', 'date_final'),
         }),
        ('LOC',
         {
             'fields': ('city', 'location'),
         }),
    )
    list_display = (
        'date_init',
        'date_final',
        'city',
        'location',
        'title',
    )
    list_display_links = (
        'date_init',
        'date_final',
        'city',
        'location',
    )
    list_editable = [
        'title',
    ]
