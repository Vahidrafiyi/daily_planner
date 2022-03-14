from django.db.models import Sum
from django.http import HttpResponseRedirect
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from account.models import Profile, SalaryReceipt, Permission, Group, Announcement
from account.serializers import RegistrationSerializer, ProfileSerializer, SalaryReceiptSerializer, \
    PermissionSerializer, GroupSerializer, AnnouncementSerializer
from eventlog.models import EnterExit
from account.permissions import IsBoss


class RegisterationAPI(APIView):
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
    def get(self, request):
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
            salary = 0
            hourly_wage = 0
            if len(user.group.all()) != 0:
                for num in range(len(user.group.all())):
                    # hourly_wage = 0
                    hourly_wage = user.group.all()[num].hourly_wage
                    salary += total_hours * float(hourly_wage)
            else:
                hourly_wage = request.data.get('hourly_wage')
                salary = total_hours * float(hourly_wage)
            # hourly_wage = user.group.all()[0].hourly_wage
            serializer.save()
            query = SalaryReceipt.objects.get(user_id=request.data.get('user'),
            to_date=request.data.get('to_date'))
            query.employee_code = user.employee_code
            query.total_hours = total_hours
            query.salary = salary
            query.hourly_wage = hourly_wage
            query.save()
            data = {}
            data['id'] = query.id
            data['user'] = request.data.get('user')
            data['hourly wage'] = hourly_wage
            data['from date'] = request.data.get('from_date')
            data['to date'] = request.data.get('to_date')
            data['total work hours'] = query.total_hours
            data['salary'] = query.salary
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AllPermissionsAPI(ListAPIView):
    permission_classes = (IsBoss,)
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

class GroupAPI(APIView):
    def get(self, request, pk):
        if len(pk) != 0:
            data = {
                'error' : 'you can not choose a specified id'
            }
            return Response(data, status=404)
        querySet = Group.objects.all()
        serializer = GroupSerializer(querySet, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        if len(pk) != 0:
            data = {
                'error' : 'you can not choose a specified id'
            }
            return Response(data, status=404)
        serializer = GroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        if len(pk) == 0:
            data={}
            data['error'] = 'you have to set a number as pk'
            return Response(data, status=404)
        else:
            query = Group.objects.get(pk=pk)
            serializer = GroupSerializer(query, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        if len(pk) == 0:
            data={}
            data['error'] = 'you have to set a number as pk'
            return Response(data, status=404)
        else:
            query = Group.objects.get(pk=pk)
            query.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

class AnnouncementAPI(APIView):
    def post(self, request):
        serializer = AnnouncementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request):
        query_set = Announcement.objects.all()
        serializer = AnnouncementSerializer(query_set, many=True)
        return Response(serializer.data, status=200)