from django.urls import include, path
from rest_framework import routers
from .views import RequestViewSet
#from

router = routers.DefaultRouter()
router.register("requests", RequestViewSet)

urlpatterns = [
    path("", include(router.urls)),
]