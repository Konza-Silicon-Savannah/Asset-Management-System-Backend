import random
import string
from django.contrib.auth.hashers import make_password
from rest_framework.serializers import ModelSerializer
from .models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        request = self.context.get("request")
        alphabets = string.ascii_letters
        plain_password = ''.join(random.choices(alphabets, k=10))
        validated_data["password"] = make_password(plain_password)
        print(plain_password)

        # TODO: add functionality to email user the Login credentials(username/email, plain_password) upon account creation

        return super().create(validated_data)