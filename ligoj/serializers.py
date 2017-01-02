from rest_framework import serializers
from taggit_serializer.serializers \
    import TagListSerializerField, TaggitSerializer
from .models import Link, TaggedLink

class LinkSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField(required=False)
    class Meta:
        model = Link

class LinkTagSerializer(serializers.ModelSerializer, ):
    tag = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='name'
     )
    tag_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = TaggedLink
        fields = ('tag', 'tag_id',)
