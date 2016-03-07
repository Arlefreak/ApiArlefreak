from . import views
from django.conf.urls import url, include
from apiArlefreak.SharedRouter import SharedRootRouter

router = SharedRootRouter()
router.register(r'posts', views.PostViewSet)
router.register(r'postImages', views.PostImageViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
