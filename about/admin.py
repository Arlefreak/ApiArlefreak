from django.contrib import admin
from .models import Entry, Image
from ordered_model.admin import OrderedModelAdmin

class ImageInline(admin.TabularInline):
    model = Image
    extra = 0

class ClientAdmin(OrderedModelAdmin):
    list_display = (
        'pk',
        'publish',
        'move_up_down_links',
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
