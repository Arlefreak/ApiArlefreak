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
    list_display = [
        'pk',
        'order',
        'slug',
        'category',
        'admin_image',
    ]
    list_display_links = [
        'pk',
        'order',
        'slug',
        'category',
        'admin_image',
    ]

@admin.register(Episode)
class EpisodeAdmin(SortableAdmin, AdminImageMixin, ViewOnSiteMixin):
    save_as = True
    list_display = [
        'pk',
        'slug',
        'podcast',
        'duration',
        'text',
        'admin_image',
    ]
    list_display_links = [
        'pk',
        'slug',
        'podcast',
        'duration',
        'text',
        'admin_image',
    ]
    list_filter = (
        'podcast',
    )
