from django.contrib import admin
from adminsortable.admin import SortableAdmin, SortableTabularInline
from embed_video.admin import AdminVideoMixin
from .models import Project, ProjectCategory, Image, Video,\
    Link, LinkCategory


class ImageInline(SortableTabularInline):
    model = Image
    extra = 0


class VideoInline(SortableTabularInline):
    model = Video
    extra = 0


class LinkInline(SortableTabularInline):
    model = Link
    extra = 0


class ProjectAdmin(SortableAdmin):
    date_hierarchy = 'date'

    list_display = (
        'pk',
        'publish',
        'name',
        'smallDescription',
        'category',
        'image_img',
        'date',
    )
    list_display_links = (
        'name',
        'smallDescription',
        'image_img',
        'date',
    )
    list_filter = (
        'category',
        'publish',
    )
    list_editable = (
        'publish',
        'category',
    )

    inlines = [
        LinkInline,
        ImageInline,
        VideoInline
    ]


class ProjectCategoryAdmin(SortableAdmin):
    list_display = (
        'pk',
        'name',
        'smallDescription',
        'image_img',
    )
    list_display_links = (
        'name',
        'smallDescription',
        'image_img',
    )


class ImageAdmin(SortableAdmin):
    list_display = (
        'pk',
        'publish',
        'project',
        'name',
        'caption',
        'imgType',
        'image_img',
    )
    list_display_links = (
        'name',
        'caption',
        'image_img',
    )
    list_editable = (
        'publish',
        'project',
        'imgType',
    )
    list_filter = (
        'project',
        'publish',
    )


class VideoAdmin(AdminVideoMixin, SortableAdmin):
    list_display = (
        'pk',
        'publish',
        'project',
        'name',
        'caption',
    )
    list_display_links = (
        'name',
        'caption',
    )
    list_editable = (
        'publish',
        'project',
    )
    list_filter = (
        'project',
        'publish',
    )


class LinkAdmin(SortableAdmin):
    list_display = (
        'pk',
        'name',
        'project',
        'link',
        'category',
    )
    list_display_links = (
        'name',
        'link'
    )
    list_editable = (
        'project',
        'category',
    )
    list_filter = (
        'project',
    )


class LinkCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'image_img',
    )
    list_display_links = (
        'name',
        'image_img'
    )

admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectCategory, ProjectCategoryAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Link, LinkAdmin)
admin.site.register(LinkCategory, LinkCategoryAdmin)
