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

        # Prepare email content
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
        recipient_list = [user.email]

        # Send email
        send_mail(
            subject,
            message,
            None,  # From email (None uses DEFAULT_FROM_EMAIL)
            recipient_list,
            fail_silently=False,
        )

        return user


        
        # print(plain_password)

        
        # TODO: add functionality to email user the Login credentials(username/email, plain_password) upon account creation

        # return super().create(validated_data)