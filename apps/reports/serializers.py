from rest_framework import serializers
from apps.assets.models import Asset
from apps.requests.models import Request
from apps.users.serializers import UserSerializer


class RequestedAssetSerializer(serializers.ModelSerializer):
    requested_user = UserSerializer()

    class Meta:
        model = Request
        fields = "__all__"

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        return {k: v for k, v in rep.items() if v not in [None, "", [], {}]}

class AssetReportSerializer(serializers.ModelSerializer):
    latest_request = serializers.SerializerMethodField()

    class Meta:
        model = Asset
        fields = "__all__"

    def get_latest_request(self, obj):
        if hasattr(obj, 'latest_request') and obj.latest_request:
            serialized = RequestedAssetSerializer(obj.latest_request).data
            return serialized if serialized else None
        return None
