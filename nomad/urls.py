from . import views
from django.conf.urls import url, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'city', views.CityViewSet)
router.register(r'trip', views.TripViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
