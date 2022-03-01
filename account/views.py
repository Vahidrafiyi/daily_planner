import datetime
from django.contrib.auth import logout
from django.db.models import Sum
from django_jalali.serializers.serializerfield import JDateField
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken

from account.models import SignUp, Profile, SalaryReceipt
from account.serializers import RegistrationSerializer, Login, ProfileSerializer, SalaryReceiptSerializer
from eventlog.models import EnterExit


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

class SalaryReceiptAPI(APIView):
    def get(self, request, pk):
        total_seconds = EnterExit.objects.filter(user_id=pk, is_paid=False).aggregate(total_seconds = Sum('work_time'))
        total_hours = total_seconds['total_seconds'].total_seconds() / 3600
        hourly_wage = Profile.objects.get(user_id=pk).hourly_wage
        print(hourly_wage)
        employee_code = Profile.objects.get(user_id=pk).employee_code
        salary = (total_hours) * hourly_wage
        query = SalaryReceipt.objects.create(
            user_id=pk, payment_date=datetime.date.today(),
            employee_code=employee_code,
            total_hours=total_hours, salary=salary
        )
        data = {}
        data['id'] = query.id
        data['user'] = query.user.username
        data['hourly wage'] = hourly_wage
        data['total work hours'] = total_hours
        data['salary'] = salary
        data['payment day'] = query.payment_date
        data['salary receipt code'] = query.employee_code
        # if data.is_valid():
        #     return data
        serializer = SalaryReceiptSerializer(query, data)
        return Response(data, status=status.HTTP_200_OK)


