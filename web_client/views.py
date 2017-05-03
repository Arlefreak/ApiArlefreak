from rest_framework.views import APIView
from rest_framework.response import Response

from .models import SiteConfiguration

config = SiteConfiguration.get_solo()

class SiteConfiguration(APIView):
    permission_classes = []

    def get(self, request, format=None):
        return Response({
            'name': config.site_name,
            'default_description': config.default_description,
            'default_preview': config.default_preview.url,
        })
