from django.urls import include, path
from rest_framework import routers
from .views import AssetViewSet
from . import views

router = routers.DefaultRouter()
router.register("assets", AssetViewSet)

urlpatterns = [
    path("", include(router.urls)),
    # path('assets/', views.AssetViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('asset-types/', views.asset_types, name='asset_types'),
    path('locations/', views.locations, name='locations'),
    path('departments/', views.departments, name='departments'),
    path('status-list/', views.status_list, name='status_list'),

]