from . import views
from django.conf.urls import url, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSet)
router.register(r'postImages', views.PostImageViewSet)
router.register(r'postTags', views.PostTagViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
