
from django.conf import settings
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import Request
from .serializers import RequestSerializer
from ..utils.token import JWTAuthentication


# Create your views here.


class RequestViewSet(ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
