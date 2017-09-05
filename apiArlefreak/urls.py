from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(
        r'^api-auth/',
        include(
            'rest_framework.urls',
            namespace='rest_framework'
        )
    ),
    url(r'^portfolio/', include('portfolio.urls')),
    url(r'^ligoj/', include('ligoj.urls')),
    url(r'^diary/', include('diary.urls')),
    url(r'^about/', include('about.urls')),
    url(r'^web_client/', include('web_client.urls')),
    url(r'^podcast/', include('podcast.urls')),
    url(r'^cv/', include('cv.urls')),
    url(r'^nomad/', include('nomad.urls')),
]
