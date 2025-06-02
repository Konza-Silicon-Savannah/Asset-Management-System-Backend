import jwt
from datetime import datetime, timedelta
from django.conf import settings
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Asset
from .serializers import AssetSerializer
from ..utils.token import JWTAuthentication


# Create your view here.

class AssetViewSet(ModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get'], url_path='available')
    def available_assets(self, request):
        available = Asset.objects.exclude(status__in=['disposal', 'damaged'])

        asset_type = request.GET.get("type")
        if asset_type and asset_type != "all":
            available = available.filter(type=asset_type)

        search = request.GET.get("search")
        if search:
            available = available.filter(Q(name__icontains=search) | Q(model__icontains=search)| Q(serial_no__icontains=search) | Q(asset_tag__icontains=search))

        serializer = self.get_serializer(available, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'], url_path='types')
    def available_asset_types(self, request):
        types = Asset.objects.values_list('type', flat=True).distinct()
        return Response(sorted(set(filter(None, types))), status=status.HTTP_200_OK)
