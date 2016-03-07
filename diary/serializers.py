from rest_framework import serializers
from taggit_serializer.serializers \
    import TagListSerializerField, TaggitSerializer
from .models import Post, Image

class PostSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField(required=False)
    class Meta:
        model = Post

class ImageSerializer(serializers.ModelSerializer):
    thumbnail = serializers.ImageField(read_only=True)
    thumbnailBW = serializers.ImageField(read_only=True)
    class Meta:
        model = Image
