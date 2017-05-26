from rest_framework import serializers
from .models import Podcast, Episode, TaggedPodcast

from taggit.models import Tag
from taggit_serializer.serializers \
    import TagListSerializerField, TaggitSerializer

class PodcastSerializer(serializers.ModelSerializer):
    tags = TagListSerializerField(required=False)
    feed = serializers.ReadOnlyField()
    class Meta:
        fields = '__all__'
        model = Podcast

class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Episode

class PodcastTagSerializer(serializers.ModelSerializer, ):
    tag = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='name'
     )
    tag_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = TaggedPodcast
        fields = ('tag_id', 'tag')
