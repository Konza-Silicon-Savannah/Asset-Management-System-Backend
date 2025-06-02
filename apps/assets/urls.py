from django.urls import include, path
from rest_framework import routers
from .views import AssetViewSet
#yes

router = routers.DefaultRouter()
router.register("assets", AssetViewSet)

urlpatterns = [
    path("", include(router.urls)),

]