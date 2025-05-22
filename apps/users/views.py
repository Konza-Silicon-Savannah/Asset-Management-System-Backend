import jwt
from datetime import datetime, timedelta
from django.contrib.auth.hashers import check_password
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.generics import ListCreateAPIView
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializers import UserSerializer
from rest_framework.authentication import BaseAuthentication


# Create your views here.

class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return None

        try:
            token = auth_header.split(" ")[1]
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"], options={"verify_exp": True})
            user = User.objects.get(id=payload["id"])
            return (user, None)
        except:
            raise AuthenticationFailed("Invalid token")

class AuthUser(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_authenticators(self):
        if self.request.method == "GET":
            return [JWTAuthentication()]
        return []

    def get_permissions(self):
        if self.request.method == "GET":
            return [IsAuthenticated()]
        return []

    def get(self, request, *args, **kwargs):
        return Response({
            "data": request.user.id
        }, status=200)

    def create(self, request, *args, **kwargs):
        data = JSONParser().parse(request)
        email = data['email']
        password = data['password']

        try:
            user = get_object_or_404(User, email=email)
        except:
            return Response({
                "message": "Email does not exist"
            }, status=404)

        if not check_password(password, user.password):
            return Response({
                "message": "Incorrect password"
            }, status=400)

        if not user.is_active:
            return Response({
                "message": "Account is suspended. Contact Admin"
            }, status=400)

        token = jwt.encode(
            {"id": str(user.id), "exp": datetime.utcnow() + timedelta(days=1)},
            settings.SECRET_KEY,
            algorithm="HS256"
        )
        return Response({
            "token": token,
            "is_admin": user.is_admin,
            "is_superuser": user.is_superuser
        }, status=200)

class UserViewSet(ModelViewSet):
    queryset = User.objects.all().order_by("-created_at")
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]