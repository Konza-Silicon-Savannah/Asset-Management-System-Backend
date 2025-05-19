import jwt
from datetime import datetime, timedelta
from django.contrib.auth.hashers import check_password
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializers import UserSerializer

# Create your views here.

@api_view(["POST"])
def sign_in(request):
    data = JSONParser().parse(request)
    username = data['username']
    password = data['password']

    try:
        user = get_object_or_404(User, username=username)
    except:
        return Response({
            "message": "Username does not exist"
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
