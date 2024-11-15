from rest_framework import serializers

from habits.models import Habit
from habits.validators import (
    ChoiceRewardValidator,
    DurationValidator,
    PleasantHabitValidator,
    PeriodicityValidator,
    AbsenceValidator,
)
from users.serializers import UserSerializer


class HabitSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Habit
        fields = "__all__"
        validators = [
            ChoiceRewardValidator("related_habit", "reward"),
            DurationValidator("duration"),
            PleasantHabitValidator("related_habit", "pleasant_habit_sign"),
            PeriodicityValidator("periodicity"),
            AbsenceValidator("reward", "related_habit", "pleasant_habit_sign"),
        ]
