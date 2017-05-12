from rest_framework import serializers
from taggit_serializer.serializers \
    import TagListSerializerField, TaggitSerializer
from .models import Post, Image, TaggedPost

class PostSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField(required=False)
    class Meta:
        model = Post

class ImageSerializer(serializers.ModelSerializer):
    thumbnail = serializers.ImageField(read_only=True)
    thumbnailBW = serializers.ImageField(read_only=True)
    class Meta:
        model = Image

class PostTagSerializer(serializers.ModelSerializer):
    tag = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='name'
     )
    tag_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = TaggedPost
        fields = ('tag', 'tag_id',)
