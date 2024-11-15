from django.urls import path

from habits.apps import HabitsConfig
from habits.views import (
    HabitListAPIView,
    HabitCreateAPIView,
    HabitPublishedListAPIView,
    HabitRetrieveAPIView,
    HabitUpdateAPIView,
    HabitDestroyAPIView,
)

app_name = HabitsConfig.name

urlpatterns = [
    path("habits/", HabitListAPIView.as_view(), name="habits_list"),
    path(
        "habits_published/",
        HabitPublishedListAPIView.as_view(),
        name="habits_published",
    ),
    path("create/", HabitCreateAPIView.as_view(), name="create"),
    path("<int:pk>/", HabitRetrieveAPIView.as_view(), name="habit_retrieve"),
    path("<int:pk>/update/", HabitUpdateAPIView.as_view(), name="habit_update"),
    path("<int:pk>/delete/", HabitDestroyAPIView.as_view(), name="habit_delete"),
]
