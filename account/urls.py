from django.urls import path, re_path
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt import views as jwt_views
from account.views import RegisterationAPI, Logout, ProfileAPI, SalaryReceiptAPI, AllPermissionsAPI, GroupAPI, \
    AnnouncementAPI

app_name = 'account'
urlpatterns = [
    path('signup/', RegisterationAPI.as_view()),
    # path('login/', ObtainAuthToken.as_view(), name='login'),
    # path('logout/', Logout.as_view()),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', ProfileAPI.as_view(), name='profile'),
    path('salary-receipt/', SalaryReceiptAPI.as_view()),
    path('permissions/', AllPermissionsAPI.as_view()),
    re_path(r"groups/(?P<pk>[0-9]*)", GroupAPI.as_view()),
    path('announcement/', AnnouncementAPI.as_view())
    # path('create-group/', GroupAPI.as_view()),
    # path('delete-group/<int:pk>', GroupAPI.as_view()),
    # path('update-group/<int:pk>', GroupAPI.as_view()),
]