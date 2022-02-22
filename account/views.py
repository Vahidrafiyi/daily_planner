from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from account.models import SignUp
from account.serializers import RegistrationSerializer

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