from django.contrib.auth.models import User
from rest_framework import serializers

from account.models import SignUp, Profile, SalaryReceipt, Permission, Group
from django_jalali.serializers.serializerfield import JDateField, JDateTimeField


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model = SignUp
        fields = ['username','email', 'password', 'password2']
        extra_kwargs = {
                    'password': {'write_only':True}
        }

    def save(self):
        account = User(
            username=self.validated_data['username'],
            email=self.validated_data['email']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must be match.'})
        if len(password) < 8 :
            raise serializers.ValidationError({'password': 'Passwords must be at least 8 characters'})
        account.set_password(password)
        account.save()
        return account


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ['user']

class SalaryReceiptSerializer(serializers.ModelSerializer):
    from_date = JDateField()
    to_date = JDateField()
    class Meta:
        model = SalaryReceipt
        fields = ['user','from_date', 'to_date', 'hourly_wage']

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'