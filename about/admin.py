from django.contrib import admin
from .models import Entry, Image
from adminsortable.admin import SortableAdmin, SortableTabularInline

class ImageInline(SortableTabularInline):
    model = Image
    extra = 0

class ClientAdmin(SortableAdmin):
    list_display = (
        'pk',
        'publish',
        'name',
        'text',
        'dateCreated',
        'dateUpdated',
    )
    list_display_links = (
        'name',
        'text',
        'dateCreated',
        'dateUpdated',
    )
    list_editable = [
        'publish',
    ]
    inlines = [
        ImageInline
    ]


admin.site.register(Entry, ClientAdmin)
admin.site.register(Image)
