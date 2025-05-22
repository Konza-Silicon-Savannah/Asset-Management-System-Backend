
from django.conf import settings
from rest_framework.viewsets import ModelViewSet
from .models import Request
from .serializers import RequestSerializer

# Create your views here.


class RequestViewSet(ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
