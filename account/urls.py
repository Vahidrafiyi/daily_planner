from django.urls import path
from account.views import RegisterationAPI
urlpatterns = [
    path('sign-up/', RegisterationAPI.as_view())
]