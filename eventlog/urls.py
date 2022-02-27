from django.urls import path

from eventlog.views import EnterExitAPI

urlpatterns = [
    path('user-log/', EnterExitAPI.as_view()),
]