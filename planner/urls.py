from django.urls import path
from planner.views import DailyPlannerAPI
urlpatterns = [
    path('today-plan/<str:username>', DailyPlannerAPI.as_view())
]