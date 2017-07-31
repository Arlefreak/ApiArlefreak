from django.contrib import admin
from .models import CV, Section, SectionOrder
from adminsortable.admin import SortableAdmin
from django.utils.html import linebreaks

class SectionInline(admin.TabularInline):
    model = SectionOrder
    list_display = ('name', 'text')
    extra = 1

@admin.register(CV)
class CVAdmin(SortableAdmin):
    list_display = (
        'order',
        'publish',
        'name',
        'get_sections',
    )
    list_display_links = (
        'order',
        'name',
        'get_sections',
    )
    list_editable = [
        'publish',
    ]
    inlines = (SectionInline,)
    def get_sections(self, obj):
        return linebreaks("\n".join([p.name for p in obj.sections.all()]))
    get_sections.allow_tags = True
    get_sections.short_description = u'Sections'
    get_sections.admin_ordering_field = 'Sections'

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
