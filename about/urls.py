from . import views
from django.conf.urls import url, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'entry', views.EntryViewSet)
router.register(r'entryImages', views.EntryImageViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
