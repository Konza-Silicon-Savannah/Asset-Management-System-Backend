
from django.conf import settings
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import Request
from .serializers import RequestSerializer, ReadRequestSerializer
from ..utils.token import JWTAuthentication


# Create your view here.


class RequestViewSet(ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.is_admin:
            return Request.objects.all()
        return Request.objects.filter(requested_user=user)

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ReadRequestSerializer
        else:
            return RequestSerializer

