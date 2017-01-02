from . import views
from django.conf.urls import url, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'link', views.LinkViewSet)
router.register(r'linkTags', views.LinkTagViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
