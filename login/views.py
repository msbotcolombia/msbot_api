# Django Rest Framework imports
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import authentication, permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
# JWT Auth
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate, login
from django.http import Http404

from .serializers import AdminUserSerializer
from .authentication import CustomJWTAuthentication
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import AdminUserSerializer
from .authentication import CustomJWTAuthentication
from django.contrib.auth import get_user_model

# Models imports
# from .models import UserProfile
from .models import AdminUser
# Serializers imports
from .serializers import AdminUserSerializer

# CreateUserView: This is a API View for creating a User with Basic Auth on DRF

class CreateUserView(APIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        serializer = AdminUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            token = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
            return Response(token, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# LoginView: This is a API View for logging a User with Basic Auth on DRF

class LoginView(APIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        serializer = TokenObtainPairSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.validated_data
        return Response(token, status=status.HTTP_200_OK)


        
# UserListView: This is a API View for reading a User list that was created on DRF

class UserListView(APIView):
    
    def get(self, request):
        users = AdminUser.objects.all()
        serializer =AdminUserSerializer(users, many=True)
        return Response(serializer.data)
    
    
# Get Token View: This is a API View for reading the Username and Password for returning the JWT Token

class MyTokenObtainPairView(TokenObtainPairView):
    permission_classes = [AllowAny]


