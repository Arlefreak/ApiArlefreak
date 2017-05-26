from django.contrib import admin
from .models import *
from adminsortable.admin import SortableAdmin, SortableTabularInline

@admin.register(Podcast)
class PodcastAdmin(SortableAdmin):
    view_on_site = True
    list_display = [
        'pk',
        'order',
        'title',
        'slug',
        'category'
    ]
    list_display_links = [
        'pk',
        'order',
        'title',
        'slug',
        'category'
    ]

@admin.register(Episode)
class PodcastAdmin(SortableAdmin):
    pass
