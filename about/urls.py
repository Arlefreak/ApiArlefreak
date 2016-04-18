from . import views
from django.conf.urls import url, include
from rest_framework import routers

router = routers.SimpleRouter()

urlpatterns = [
    url(r'^', include(router.urls)),
]
