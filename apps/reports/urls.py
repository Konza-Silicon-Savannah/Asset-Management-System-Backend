from django.urls import include, path
from .views import reports, asset_types

urlpatterns = [
    path("reports", reports),
    path("asset-types", asset_types)
]