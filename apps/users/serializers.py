import random
import string
from django.contrib.auth.hashers import make_password
from rest_framework.serializers import ModelSerializer
from django.core.mail import send_mail
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
        plain_password = ''.join(random.choices(alphabets, k=10))
        validated_data["password"] = make_password(plain_password)

        user = super().create(validated_data)

        subject = "Your Account Credentials"
        message = (
            f"Hello {user.username},\n\n"
            f"Your account has been created successfully.\n"
            f"Here are your login credentials:\n"
            f"Username: {user.username}\n"
            f"Email: {user.email}\n"
            f"Password: {plain_password}\n\n"
            "Please change your password after logging in."
        )

        try:
            send_mail(
                subject,
                message,
                None,
                [user.email],
                fail_silently=False,
            )
        except Exception as e:
            print(e)

        return user