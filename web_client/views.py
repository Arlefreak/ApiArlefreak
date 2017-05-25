from rest_framework import permissions
from rest_framework import viewsets

from .models import SiteConfiguration
from .serializers import SiteConfigurationSerializer

class SiteConfigurationViewSet(viewsets.ModelViewSet):
    queryset = SiteConfiguration.objects.all()
    serializer_class = SiteConfigurationSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

# class SiteConfigurationViewSet(APIView):
#     permission_classes = []

#     def get(self, request, format=None):
#         config = SiteConfiguration.get_solo()
#         return Response({
#             'title': config.site_name,
#             'description': config.default_description,
#             'preview': config.default_preview.url,
#             'longDescription': config.long_description,
#             'subscribeDescription': config.email_subscription,
#             'mail': config.mail,
#             'twitter': config.twitter,
#             'github': config.github,
#             'linkdn': config.linkdn,
#         })
