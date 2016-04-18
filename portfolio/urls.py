from . import views
from django.conf.urls import url, include
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'projects', views.ProjectViewSet)
router.register(r'projectsCategories', views.ProjectCategoryViewSet)
router.register(r'projectsLinks', views.ProjectLinkViewSet)
router.register(r'projectsImages', views.ProjectImageViewSet)
router.register(r'tags', views.TagViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
