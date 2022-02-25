from django.urls import path
from planner.views import AllPlan, TaskAPI, UserAPI

urlpatterns = [
    path('today-plan/<str:username>', AllPlan.as_view()),
    path('enter-today-plan/', AllPlan.as_view()),
    path('edit-today-plan/<str:username>', AllPlan.as_view()),
    path('tasks/', TaskAPI.as_view()),
    path('users/', UserAPI.as_view()),
    # path('today-plan/beverage', BeverageCreate.as_view()),
]