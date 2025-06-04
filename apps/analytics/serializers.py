from rest_framework import serializers

class AnalyticsSerializer(serializers.Serializer):
    total_assets = serializers.IntegerField()
    assets_due_for_disposal = serializers.IntegerField()
    pending_asset_requests = serializers.IntegerField()
    approved_assets = serializers.IntegerField()

class MonthlyGraphsSerializer(serializers.Serializer):
    month = serializers.CharField()
    approved_assets = serializers.IntegerField()
    pending_requests = serializers.IntegerField()
    disposal = serializers.IntegerField()

