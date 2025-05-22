from django.urls import include, path
from rest_framework import routers
from .views import UserViewSet, AuthUser

router = routers.DefaultRouter()
router.register("users", UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("auth", AuthUser.as_view())
]