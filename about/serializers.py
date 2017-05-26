from rest_framework import serializers
from taggit_serializer.serializers \
    import TagListSerializerField, TaggitSerializer
from .models import Entry, Image

class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Entry

class ImageSerializer(serializers.ModelSerializer):
    thumbnail = serializers.ImageField(read_only=True)
    thumbnailBW = serializers.ImageField(read_only=True)
    class Meta:
        fields = '__all__'
        model = Image
