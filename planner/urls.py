from django.urls import path
from planner.views import UserAPI, EnterTaskAPI, EnterPlan, EnterSubTaskAPI, \
    EnterTodayGoalAPI, DrinkAPI, EnterDoneGoalAPI

urlpatterns = [
    # daily plan
    path('today-plan/', EnterPlan.as_view()),
    # path('today-plan/', AllPlan.as_view()),
    # path('edit-today-plan/', AllPlan.as_view()),
    # Task
    path('today-task/', EnterTaskAPI.as_view()),
    # path('today-task/', TaskAPI.as_view()),
    # path('edit-today-task/', TaskAPI.as_view()),
    # SubTask
    path('today-subtask/', EnterSubTaskAPI.as_view()),
    # path('today-subtask/<str:username>', SubTaskAPI.as_view()),
    # path('edit-today-subtask/<str:username>', SubTaskAPI.as_view()),
    # TodayGoal
    path('today-goal/', EnterTodayGoalAPI.as_view()),
    # path('today-goal/', ShowTodayGoalAPI.as_view()),
    # path('edit-today-goal/', EnterTodayGoalAPI.as_view()),
    # Drink
    path('drink/', DrinkAPI.as_view()),
    # path('tasks/', TaskAPI.as_view()),
    path('users/', UserAPI.as_view()),
    # path('today-plan/beverage', BeverageCreate.as_view())
    path('done-goal/<int:pk>', EnterDoneGoalAPI.as_view())

]

