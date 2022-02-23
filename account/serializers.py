from django.contrib.auth.models import User
from rest_framework import serializers

from account.models import SignUp,LogIn

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

class Login(serializers.ModelSerializer):
    class Meta:
        model = LogIn
        fields = ['id','username', 'password']
        extra_kwargs = {
            'password': {'write_only':True}
        }