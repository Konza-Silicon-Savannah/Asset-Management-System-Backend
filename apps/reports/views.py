import os

from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Q
from datetime import timedelta
from django.utils import timezone

from apps.assets.models import Asset
from apps.reports.serializers import AssetReportSerializer
from apps.requests.models import Request
from apps.utils.token import JWTAuthentication


@api_view(["GET"])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def reports(request):
    assets = Asset.objects.all()

    asset_type = request.GET.get("type")
    if asset_type and asset_type != "all":
        assets = assets.filter(type=asset_type)

    date_range = request.GET.get("date_range")
    if date_range:
        try:
            days = int(date_range)
            since_date = timezone.now() - timedelta(days=days)
            assets = assets.filter(created_at__gte=since_date)
        except ValueError:
            pass

    search = request.GET.get("search")
    if search:
        assets = assets.filter(Q(name__icontains=search) | Q(model__icontains=search))

    # Apply pagination
    paginator = PageNumberPagination()
    paginator.page_size = int(os.getenv("PAGE_SIZE", 10))  # fallback to 10 if PAGE_SIZE not set
    paginated_assets = paginator.paginate_queryset(assets, request)

    # Add latest request info
    asset_map = {}
    for asset in paginated_assets:
        latest = Request.objects.filter(requested_asset=asset).order_by('-requested_date').select_related(
            'requested_user').first()
        asset.latest_request = latest
        asset_map[asset.id] = asset

    serializer = AssetReportSerializer(paginated_assets, many=True)
    return paginator.get_paginated_response(serializer.data)
