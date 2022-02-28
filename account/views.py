from django.contrib.auth import logout
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken

from account.models import SignUp, Profile
from account.serializers import RegistrationSerializer, Login, ProfileSerializer


class RegisterationAPI(APIView):
    # authentication_classes = (None,)
    permission_classes = (AllowAny,)
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'seccessfully registered a new user'
            data['username'] = account.username
            data['email'] = account.email
        else:
            data = serializer.errors
        return Response(data)

class LoginAPI(APIView):
    def post(self, request):
        serializer = Login(data=request.data)
        data = {}
        if serializer.is_valid():
            token = Token.objects.get_or_create(user=request.user)
            data['token'] = token
            data['username'] = request.user.username
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Logout(APIView):
    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        data = {}
        data['logout'] = f'{request.user.username} logged out and its token deleted'
        return Response(data, status=status.HTTP_200_OK)

class ProfileAPI(APIView):
    def get(self, request):
        query = Profile.objects.get(user=request.user)
        serializer = ProfileSerializer(query)
        return Response(status=status.HTTP_200_OK)

    def patch(self, request):
        query = Profile.objects.get(user=request.user)
        serializer = ProfileSerializer(query, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

