from rest_framework import serializers
from taggit_serializer.serializers \
    import TagListSerializerField, TaggitSerializer
from .models import Project, ProjectCategory


class ProjectSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField(required=False)

    class Meta:
        model = Project


class ProjectCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectCategory
