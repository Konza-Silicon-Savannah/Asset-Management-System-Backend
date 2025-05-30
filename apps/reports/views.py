from datetime import timedelta
from django.utils import timezone
from django.db.models import Q
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from apps.assets.models import Asset
from apps.reports.serializers import AssetReportSerializer
from apps.requests.models import Request
from apps.utils.token import JWTAuthentication


# Create your views here.

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

    asset_map = {}
    for asset in assets:
        latest = Request.objects.filter(requested_asset=asset).order_by('-requested_date').select_related(
            'requested_user').first()
        asset.latest_request = latest
        asset_map[asset.id] = asset

    serializer = AssetReportSerializer(assets, many=True)
    return Response(serializer.data)