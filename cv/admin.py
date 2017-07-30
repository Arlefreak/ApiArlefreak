from django.contrib import admin
from .models import CV, Section, SectionOrder
from adminsortable.admin import SortableAdmin

class SectionInline(admin.TabularInline):
    model = SectionOrder
    list_display = ('name', 'text')
    extra = 0

@admin.register(CV)
class CVAdmin(SortableAdmin):
    list_display = (
        'pk',
        'order',
        'publish',
        'name',
    )
    list_display_links = (
        'pk',
        'order',
        'name',
    )
    list_editable = [
        'publish',
    ]
    inlines = (SectionInline,)

@admin.register(Section)
class SectionAdmin(SortableAdmin):
    list_display = (
        'pk',
        'name',
        'text',
    )
    list_display_links = (
        'pk',
        'name',
        'text',
    )
