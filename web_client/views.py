from rest_framework.views import APIView
from rest_framework.response import Response

from .models import SiteConfiguration

class SiteConfigurationViewSet(APIView):
    permission_classes = []

    def get(self, request, format=None):
        config = SiteConfiguration.get_solo()
        return Response({
            'title': config.site_name,
            'description': config.default_description,
            'preview': config.default_preview.url,
            'longDescription': config.long_description,
            'mail': config.mail,
            'twitter': config.twitter,
            'github': config.github,
            'linkdn': config.linkdn,
        })
