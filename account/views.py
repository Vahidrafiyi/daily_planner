import datetime
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.redirects.models import Redirect
from django.http.response import HttpResponseRedirectBase
from django.shortcuts import redirect
from django.db.models import Sum
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django_jalali.serializers.serializerfield import JDateField
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.reverse import reverse, reverse_lazy
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth import views
from account.models import SignUp, Profile, SalaryReceipt
from account.serializers import RegistrationSerializer, ProfileSerializer, SalaryReceiptSerializer
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
            return HttpResponseRedirect(redirect_to='http://127.0.0.1:8000/log/all-user-log/', status=302)
        else:
            data = serializer.errors
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

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
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request):
        query = Profile.objects.get(user=request.user)
        # data = request.data

        # try:
        #     user = User.objects.get(id=request.user.id)
        #     user.save()
        #
        # except KeyError:
        #     pass
        # query.first_name = data.get('first_name', query.first_name)
        # query.last_name = data.get('last_name', query.last_name)
        # query.email = data.get('email', query.email)
        # query.gender = data.get('gender', query.gender)
        # query.code_melli = data.get('code_melli', query.code_melli)
        # query.code_passport = data.get('code_passport', query.code_passport)
        # query.father_name = data.get('father_name', query.father_name)
        # query.image = data.get('image', query.image)
        # query.phone = data.get('phone', query.phone)
        # query.emergency_phone = data.get('emergency_phone', query.emergency_phone)
        serializer = ProfileSerializer(query, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SalaryReceiptAPI(APIView):
    def post(self, request):
        serializer = SalaryReceiptSerializer(data=request.data)
        if serializer.is_valid():
            total_seconds = EnterExit.objects.filter(user_id=request.data.get('user'), is_paid=False, date__range=[request.data.get('from_date'), request.data.get('to_date')]).aggregate(
                total_seconds=Sum('work_time'))
            user = Profile.objects.get(user_id=request.data.get('user'))
            total_hours = total_seconds['total_seconds'].total_seconds() / 3600
            salary = total_hours * float(request.data.get('hourly_wage'))
            serializer.save()
            query = SalaryReceipt.objects.get(user_id=request.data.get('user'),
            to_date=request.data.get('to_date'))
            query.employee_code = user.employee_code
            query.total_hours = total_hours
            query.salary = salary
            # updated_query = query.update(
            #     employee_code=user.employee_code,
            #     total_hours=total_hours,
            #     salary=salary
            # )
            query.save()
            print(query)
            data = {}
            data['id'] = query.id
            data['user'] = request.data.get('user')
            data['hourly wage'] = request.data.get('hourly_wage')
            data['from date'] = request.data.get('from_date')
            data['to date'] = request.data.get('to_date')
            data['total work hours'] = query.total_hours
            data['salary'] = query.salary
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def get(self, request, pk):
    #     SalaryReceipt.objects.
    #     total_seconds = EnterExit.objects.filter(user_id=pk, date__gt=).aggregate(total_seconds = Sum('work_time'))
    #     total_hours = total_seconds['total_seconds'].total_seconds() / 3600
    #     hourly_wage = Profile.objects.get(user_id=pk).hourly_wage
    #     print(hourly_wage)
    #     employee_code = Profile.objects.get(user_id=pk).employee_code
    #     salary = (total_hours) * hourly_wage
    #     query = SalaryReceipt.objects.create(
    #         user_id=pk, payment_date=datetime.date.today(),
    #         employee_code=employee_code,
    #         total_hours=total_hours, salary=salary
    #     )
    #     data = {}
    #     data['id'] = query.id
    #     data['user'] = query.user.username
    #     data['hourly wage'] = hourly_wage
    #     data['total work hours'] = total_hours
    #     data['salary'] = salary
    #     data['payment day'] = query.payment_date
    #     data['salary receipt code'] = query.employee_code
    #     serializer = SalaryReceiptSerializer(query, data)
    #     return Response(data, status=status.HTTP_200_OK)


# {
# "username":"taha",
# "email":"taha@yahoo.com",
# "password":"taha1234",
# "password2":"taha1234"
# }