from django.contrib import admin
from .models import Link

def LinkSetAct(modeladmin, request, queryset):
    # queryset.update(status='ACT')
    for obj in queryset:
        obj.status = 'ACT'
        obj.save()
LinkSetAct.short_description = "Set Active"

def LinkSetHidden(modeladmin, request, queryset):
    for obj in queryset:
        obj.status = 'HID'
        obj.save()
LinkSetHidden.short_description = "Set Hidden"

class LinkAdmin(admin.ModelAdmin):
    save_on_top = True
    actions = [LinkSetAct, LinkSetHidden]
    list_display = (
        'date_created',
        'status',
        'name',
        'tag_list',
        'date_updated',
    )
    list_display_links = (
        'name',
        'date_created',
        'date_updated',
    )
    list_editable = [
        'status',
    ]

    def get_queryset(self, request):
        return super(LinkAdmin, self).get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())

admin.site.register(Link, LinkAdmin)
