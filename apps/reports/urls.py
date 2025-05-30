from django.urls import include, path
from .views import reports

urlpatterns = [
    path("reports", reports),
]