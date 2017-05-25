# from .custom_routers import HybridRouter
from rest_framework import routers
from django.conf.urls import url, include
from . import views

# router = HybridRouter()
# router.add_api_view(
#     'config',
#     url(r'^config/$', views.SiteConfigurationViewSet.as_view(), 
#         name='site_configuration'))

router = routers.DefaultRouter()
router.register(r'^config', views.SiteConfigurationViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
