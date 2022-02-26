from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken

from account.views import RegisterationAPI, LoginAPI, Logout

urlpatterns = [
    path('sign-up/', RegisterationAPI.as_view()),
    path('login/', ObtainAuthToken.as_view()),
    path('logout/', Logout.as_view())
]