from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from drf_spectacular.utils import extend_schema
from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import RegistrationSerializer, LoginSerializer


class LoginView(APIView):
    @extend_schema(
        request=LoginSerializer,
        responses={200: {'token': 'example_token', 'is_superuser': False}}
    )
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        login(request, user)

        token, created = Token.objects.get_or_create(user=user)
        is_superuser = user.is_superuser

        return Response({'token': f'Token {token.key}', 'is_superuser': is_superuser})


class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({'message': 'Successfully logged out'})


class RegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer
