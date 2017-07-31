from rest_framework import serializers
from .models import SiteConfiguration

class SiteConfigurationSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='site_name')
    description = serializers.CharField(source='default_description')
    preview = serializers.ImageField(source='default_preview')
    longDescription = serializers.CharField(source='long_description')
    subscribeDescription = serializers.CharField(source='email_subscription')
    class Meta:
        fields = (
            'title',
            'description',
            'preview',
            'longDescription',
            'subscribeDescription',
            'mail',
            'twitter',
            'github',
            'linkdn',
        )
        model = SiteConfiguration
