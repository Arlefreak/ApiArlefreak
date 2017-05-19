from django.contrib import admin
from adminsortable.admin import SortableAdmin, SortableTabularInline
from embed_video.admin import AdminVideoMixin
from .models import Post, Image, Video


class ImageInline(SortableTabularInline):
    model = Image
    extra = 0


class VideoInline(SortableTabularInline):
    model = Video
    extra = 0


class PostAdmin(SortableAdmin):
    list_display = (
        'pk',
        'publish',
        'title',
        'dateCreated',
        'image_img',
    )
    list_display_links = (
        'title',
        'dateCreated',
        'image_img',
    )
    list_filter = (
        'publish',
    )
    list_editable = (
        'publish',
    )

    inlines = [
        ImageInline,
        VideoInline
    ]


class ImageAdmin(SortableAdmin):
    list_display = (
        'publish',
        'post',
        'name',
        'caption',
        'image_img',
    )
    list_display_links = (
        'name',
        'caption',
        'image_img',
    )
    list_editable = (
        'publish',
        'post',
    )
    list_filter = (
        'post',
        'publish',
    )


class VideoAdmin(AdminVideoMixin, SortableAdmin):
    list_display = (
        'publish',
        'post',
        'name',
        'caption',
    )
    list_display_links = (
        'name',
        'caption',
    )
    list_editable = (
        'publish',
        'post',
    )
    list_filter = (
        'post',
        'publish',
    )


admin.site.register(Post, PostAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Video, VideoAdmin)
