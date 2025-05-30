from django.utils import timezone
from  rest_framework.serializers import ModelSerializer
from .models import Request

class RequestSerializer(ModelSerializer):
    class Meta:
        model = Request
        fields = "__all__"

    def create(self, validated_data):
        request = self.context.get("request")
        validated_data["requested_user"] = request.user
        # validated_data["check_out"] = timezone.now()   for admin when request is approved

        return super().create(validated_data)

class ReadRequestSerializer(ModelSerializer):
    class Meta:
        model = Request
        fields = "__all__"
        depth = 1


