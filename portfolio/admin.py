from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin
from embed_video.admin import AdminVideoMixin
from .models import Project, ProjectCategory, Image, Video,\
    Link, LinkCategory


class ImageInline(admin.TabularInline):
    model = Image
    extra = 0


class VideoInline(admin.TabularInline):
    model = Video
    extra = 0


class LinkInline(admin.TabularInline):
    model = Link
    extra = 0


class ProjectAdmin(OrderedModelAdmin):
    date_hierarchy = 'date'

    list_display = (
        'publish',
        'name',
        'smallDescription',
        'category',
        'image_img',
        'date',
        'move_up_down_links',
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


class ProjectCategoryAdmin(OrderedModelAdmin):
    list_display = (
        'name',
        'smallDescription',
        'image_img',
        'move_up_down_links',
    )
    list_display_links = (
        'name',
        'smallDescription',
        'image_img',
    )


class ImageAdmin(OrderedModelAdmin):
    list_display = (
        'publish',
        'project',
        'name',
        'caption',
        'imgType',
        'image_img',
        'move_up_down_links',
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


class VideoAdmin(AdminVideoMixin, OrderedModelAdmin):
    list_display = (
        'publish',
        'project',
        'name',
        'caption',
        'move_up_down_links',
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


class LinkAdmin(OrderedModelAdmin):
    list_display = (
        'name',
        'project',
        'link',
        'category',
        'move_up_down_links',
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
