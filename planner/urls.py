from django.urls import path
from planner.views import AllPlan, TaskAPI, UserAPI, EnterTaskAPI, EnterPlan, SubTaskAPI, EnterSubTaskAPI, \
    EnterTodayGoalAPI, ShowTodayGoalAPI, DrinkAPI, EnterDoneGoalAPI

urlpatterns = [
    # daily plan
    path('enter-today-plan/', EnterPlan.as_view()),
    path('today-plan/', AllPlan.as_view()),
    path('edit-today-plan/', AllPlan.as_view()),
    # Task
    path('enter-today-task/', EnterTaskAPI.as_view()),
    path('today-task/', TaskAPI.as_view()),
    path('edit-today-task/', TaskAPI.as_view()),
    # SubTask
    path('enter-today-subtask/', EnterSubTaskAPI.as_view()),
    path('today-subtask/<str:username>', SubTaskAPI.as_view()),
    path('edit-today-subtask/<str:username>', SubTaskAPI.as_view()),
    # TodayGoal
    path('enter-today-goal/', EnterTodayGoalAPI.as_view()),
    path('today-goal/', ShowTodayGoalAPI.as_view()),
    path('edit-today-goal/', EnterTodayGoalAPI.as_view()),
    # Drink
    path('drink/', DrinkAPI.as_view()),
    path('tasks/', TaskAPI.as_view()),
    path('users/', UserAPI.as_view()),
    # path('today-plan/beverage', BeverageCreate.as_view())
    path('done-goal/<int:pk>', EnterDoneGoalAPI.as_view())

]

