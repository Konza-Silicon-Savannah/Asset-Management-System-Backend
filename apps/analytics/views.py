from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from datetime import datetime
from calendar import month_name
from apps.assets.models import Asset
from apps.requests.models import Request
from apps.utils.token import JWTAuthentication 
from .serializers import AnalyticsSerializer, MonthlyGraphsSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def analytics(request):
    data = {
        "total_assets": Asset.objects.count(),
        "assets_due_for_disposal": Asset.objects.filter(status='disposal').count(),
        "pending_asset_requests": Request.objects.filter(action='pending').count(),
        "approved_assets": Request.objects.filter(action='approved').count(),
    }
    serializer = AnalyticsSerializer(data)
    return Response(serializer.data)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
# @authentication_classes([JWTAuthentication])
def graph(request):
    data = []
    current_year = datetime.now().year

    for index, month_str in enumerate(month_name[1:], start=1):  # month 1 to 12
        if index < 6:  # Jan to May: zero values
            data.append({
                "month": month_str,
                "approved_assets": 0,
                "pending_requests": 0,
                "disposal": 0,
            })
        else:  # June to December: actual data
            start_date = datetime(current_year, index, 1)
            if index == 12:
                end_date = datetime(current_year + 1, 1, 1)
            else:
                end_date = datetime(current_year, index + 1, 1)

            approved_assets = Request.objects.filter(
                action="approved",
                requested_date__gte=start_date,
                requested_date__lt=end_date
            ).count()

            pending_requests = Request.objects.filter(
                action="pending",
                requested_date__gte=start_date,
                requested_date__lt=end_date
            ).count()

            disposal = Asset.objects.filter(
                created_at__gte=start_date,
                created_at__lt=end_date
            ).count()

            data.append({
                "month": month_str,
                "approved_assets": approved_assets,
                "pending_requests": pending_requests,
                "disposal": disposal,
            })

    serializer = MonthlyGraphsSerializer(data, many=True)
    return Response(serializer.data)

