from . import views
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'projects', views.ProjectViewSet)
router.register(r'projectsCategories', views.ProjectCategoryViewSet)
router.register(r'projectsLinks', views.ProjectLinkViewSet)
router.register(r'images', views.ImageViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(
        r'^api-auth/',
        include(
            'rest_framework.urls',
            namespace='rest_framework'
        )
    )
]
