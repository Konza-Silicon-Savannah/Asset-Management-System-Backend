import jwt
from datetime import datetime, timedelta
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Asset
from .serializers import AssetSerializer
from ..utils.token import JWTAuthentication


# Create your views here.

class AssetViewSet(ModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
