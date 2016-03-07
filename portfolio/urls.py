from . import views
from django.conf.urls import url, include
from apiArlefreak.SharedRouter import SharedRootRouter

router = SharedRootRouter()
router.register(r'projects', views.ProjectViewSet)
router.register(r'projectsCategories', views.ProjectCategoryViewSet)
router.register(r'projectsLinks', views.ProjectLinkViewSet)
router.register(r'projectsImages', views.ProjectImageViewSet)
router.register(r'tags', views.TagViewSet)

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
