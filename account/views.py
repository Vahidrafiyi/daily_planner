from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken

from account.models import SignUp
from account.serializers import RegistrationSerializer, Login


class RegisterationAPI(APIView):
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