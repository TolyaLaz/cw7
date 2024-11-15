from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated

from habits.models import Habit
from habits.paginators import HabitPagination
from habits.serializers import HabitSerializer
from users.permissions import IsOwner


class HabitListAPIView(ListAPIView):
    serializer_class = HabitSerializer
    pagination_class = HabitPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Фильтр для списка привычек владельца."""
        user = self.request.user
        return Habit.objects.filter(owner=user)


class HabitPublishedListAPIView(ListAPIView):
    serializer_class = HabitSerializer
    pagination_class = HabitPagination

    def get_queryset(self):
        """Фильтр для списка опубликованных привычек."""
        return Habit.objects.filter(is_published=True)


class HabitCreateAPIView(CreateAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """Присваивает владельца привычки при создании."""
        habit = serializer.save()
        habit.owner = self.request.user
        habit.save()


class HabitRetrieveAPIView(RetrieveAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwner]


class HabitUpdateAPIView(UpdateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class HabitDestroyAPIView(DestroyAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]
