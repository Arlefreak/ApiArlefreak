from rest_framework import serializers
from taggit_serializer.serializers \
    import TagListSerializerField, TaggitSerializer
from .models import Link, TaggedLink

class LinkSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField(required=False)
    dateUpdated = serializers.CharField(source='date_updated', read_only=True)
    dateCreated = serializers.CharField(source='date_created', read_only=True)
    status = serializers.CharField(read_only=True)
    class Meta:
        model = Link
        fields = (
            'id',
            'tags',
            'name',
            'link', 
            'status',
            'dateCreated',
            'dateUpdated',
        )

class LinkTagSerializer(serializers.ModelSerializer):
    tag = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='name'
     )
    tag_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = TaggedLink
        fields = ('tag', 'tag_id',)
