from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken

from account.views import RegisterationAPI, Logout, ProfileAPI, SalaryReceiptAPI
app_name = 'account'
urlpatterns = [
    path('signup/', RegisterationAPI.as_view()),
    path('login/', ObtainAuthToken.as_view(), name='login'),
    path('logout/', Logout.as_view()),
    path('profile/', ProfileAPI.as_view(), name='profile'),
    path('salary-receipt/', SalaryReceiptAPI.as_view()),
]