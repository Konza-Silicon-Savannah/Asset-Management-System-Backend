from rest_framework import serializers

class AnalyticsSerializer(serializers.Serializer):
    total_assets = serializers.IntegerField()
    assets_due_for_disposal = serializers.IntegerField()
    pending_asset_requests = serializers.IntegerField()
    approved_assets = serializers.IntegerField()
