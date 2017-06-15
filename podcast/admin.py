from django.contrib import admin
from .models import *
from adminsortable.admin import SortableAdmin, SortableTabularInline

class AdminImageMixin(object):
    def admin_image(self, obj):
        return u"<img src='%s' style='height: 100px; width: auto; display: block'/>" % obj.image.url
    admin_image.allow_tags = True
    admin_image.short_description = u"Preview"

class ViewOnSiteMixin(object):
    def view_on_site(self, obj):
        return u"<a class='button' href='%s'>view on site</a>" % obj.get_absolute_url()
    view_on_site.allow_tags = True
    view_on_site.short_description = u"View on site"

@admin.register(Podcast)
class PodcastAdmin(SortableAdmin, AdminImageMixin, ViewOnSiteMixin):
    save_as = True
    fieldsets = (
        (None, {
            'fields': (
                'title',
                'image'
            )
        }),
        ('Author', {
            'fields': (
                'author',
                'author_mail'
            )
        }),
        ('Categories', {
            'fields': (
                'parent_category',
                'child_category',
            )
        }),
        (None, {
            'fields': (
                'language',
                'tags',
            )
        }),
        ('Links', {
            'fields': (
                'iTunesURL',
                'feedBurner',
            )
        }),
        ('Description', {
            'fields': (
                'small_text',
                'text',
            ),
        }),
    )
    list_display = [
        'order',
        'dateCreated',
        'slug',
        'small_text',
        'admin_image',
    ]
    list_display_links = [
        'order',
        'dateCreated',
        'slug',
        'small_text',
        'admin_image',
    ]

@admin.register(Episode)
class EpisodeAdmin(SortableAdmin, AdminImageMixin, ViewOnSiteMixin):
    save_as = True
    fieldsets = (
        (None, {
            'fields': (
                'podcast',
                'title',
                'image'
            )
        }),
        ('Files', {
            'fields': (
                'audio_mp3',
                'audio_ogg',
            )
        }),
        ('File Info', {
            'fields': (
                'audio_type',
                'duration',
                'audio_size',
            )
        }),
        ('Description', {
            'fields': (
                'small_text',
                'text',
            )
        }),
    )
    list_display = [
        'pk',
        'slug',
        'podcast',
        'duration',
        'plain_text',
        'admin_image',
    ]
    list_display_links = [
        'pk',
        'slug',
        'podcast',
        'duration',
        'admin_image',
    ]
    list_filter = (
        'podcast',
    )
