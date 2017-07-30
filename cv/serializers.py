from rest_framework import serializers
from taggit_serializer.serializers \
    import TagListSerializerField, TaggitSerializer
from .models import CV, Section

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Section

class CVSerializer(serializers.ModelSerializer):
    sections = SectionSerializer(many=True, read_only=True)
    class Meta:
        fields = '__all__'
        model = CV
