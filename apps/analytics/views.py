from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from apps.assets.models import Asset
from apps.requests.models import Request
from apps.utils.token import JWTAuthentication 
from .serializers import AnalyticsSerializer

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
# @authentication_classes([JWTAuthentication])
def analytics(request):
    data = {
        "total_assets": Asset.objects.count(),
        "assets_due_for_disposal": Asset.objects.filter(status='disposal').count(),
        "pending_asset_requests": Request.objects.filter(action='pending').count(),
        "approved_assets": Request.objects.filter(action='approved').count(),
    }
    serializer = AnalyticsSerializer(data)
    return Response(serializer.data)
