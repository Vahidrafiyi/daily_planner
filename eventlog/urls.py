from django.urls import path

from eventlog.views import EnterExitAPI, EnterExitAllAPI
app_name = 'log'
urlpatterns = [
    path('enter-exit/', EnterExitAPI.as_view()),
    path('all-user-log/', EnterExitAllAPI.as_view(), name='all user'),
]