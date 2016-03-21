from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin
from embed_video.admin import AdminVideoMixin
from .models import Post, Image, Video


class ImageInline(admin.TabularInline):
    model = Image
    extra = 0


class VideoInline(admin.TabularInline):
    model = Video
    extra = 0


class PostAdmin(OrderedModelAdmin):
    list_display = (
        'publish',
        'move_up_down_links',
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


class ImageAdmin(OrderedModelAdmin):
    list_display = (
        'publish',
        'post',
        'name',
        'caption',
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
        'post',
    )
    list_filter = (
        'post',
        'publish',
    )


class VideoAdmin(AdminVideoMixin, OrderedModelAdmin):
    list_display = (
        'publish',
        'post',
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
        'post',
    )
    list_filter = (
        'post',
        'publish',
    )


admin.site.register(Post, PostAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Video, VideoAdmin)
