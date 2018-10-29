from rest_framework import serializers
from taggit_serializer.serializers import (TaggitSerializer,
                                           TagListSerializerField)

from .models import Image, Post, TaggedPost


class PostSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField(required=False)
    mainImage = serializers.SerializerMethodField(method_name="get_main_image")

    class Meta:
        fields = '__all__'
        model = Post

    def get_main_image(self, obj):
        try:
            mainImage = Image.objects.filter(post=obj, imgType='mni')[:1].get()
            if mainImage:
                return mainImage.image.url
            else:
                return 'No Image'
        except:
            return 'No Image'


class ImageSerializer(serializers.ModelSerializer):
    thumbnail = serializers.ImageField(read_only=True)
    thumbnailBW = serializers.ImageField(read_only=True)

    class Meta:
        fields = '__all__'
        model = Image


class PostTagSerializer(serializers.ModelSerializer):
    tag = serializers.SlugRelatedField(
        many=False, read_only=True, slug_field='name')
    tag_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = TaggedPost
        fields = (
            'tag',
            'tag_id',
        )
