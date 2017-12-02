from . import views
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'projects', views.ProjectViewSet)
router.register(r'projectsCategories', views.ProjectCategoryViewSet)
router.register(r'projectsLinks', views.ProjectLinkViewSet)
router.register(r'projectsImages', views.ProjectImageViewSet)
router.register(r'projectTags', views.ProjectTagViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
