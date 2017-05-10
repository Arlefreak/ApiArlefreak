from .custom_routers import HybridRouter
from django.conf.urls import url, include
from . import views

rest_router = HybridRouter()
rest_router.add_api_view(
    'config',
    url(r'^config/$', views.SiteConfigurationViewSet.as_view(), 
        name='site_configuration'))

urlpatterns = [
    url(r'^', include(rest_router.urls), name='rest_api'),    
]
