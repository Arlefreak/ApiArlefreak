from django.conf.urls import url, include
from django.contrib import admin
from apiArlefreak.SharedRouter import SharedRootRouter
import portfolio.urls
import diary.urls

def api_urls():
    return SharedRootRouter.shared_router.urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(api_urls())),
]
