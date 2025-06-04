from django.conf import settings
from rest_framework.permissions import AllowAny  # jaymoh remove this import
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import Request
from .serializers import RequestSerializer, ReadRequestSerializer
from ..utils.token import JWTAuthentication


class RequestViewSet(ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [AllowAny]  # Allow any user for testing

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.is_admin:
            return Request.objects.all().order_by("-requested_date")
        return Request.objects.filter(requested_user=user).order_by("-requested_date")

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ReadRequestSerializer
        else:
            return RequestSerializer
    
    def update(self, request, *args, **kwargs):
        """Override update to handle status changes"""
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        
        return Response(serializer.data)
    
    def partial_update(self, request, *args, **kwargs):
        """Handle PATCH requests"""
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)