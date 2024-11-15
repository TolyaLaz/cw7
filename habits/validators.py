from datetime import timedelta

from rest_framework.exceptions import ValidationError


class ChoiceRewardValidator:
    """Исключает одновременный выбор награды и приятной привычки."""

    def __init__(self, related_habit, reward):
        self.related_habit = related_habit
        self.reward = reward

    def __call__(self, habit):
        if habit.get(self.related_habit) and habit.get(self.reward):
            raise ValidationError(
                f"""Нельзя выбрать {self.related_habit} и {self.reward} одновременно, 
                выберите награду или приятную привычку."""
            )


class DurationValidator:
    """Проверяет длительность выполнения привычки, она не должна превышать 2 минут."""

    def __init__(self, duration):
        self.duration = duration

    def __call__(self, habit):
        max_duration = timedelta(minutes=2)
        if habit.get(self.duration) and habit.get(self.duration) > max_duration:
            raise ValidationError(f"Выполнение не может длиться более {max_duration}")


class PleasantHabitValidator:
    """Проверяет, является ли привычка приятной."""

    def __init__(self, related_habit, pleasant_habit_sigh):
        self.related_habit = related_habit
        self.pleasant_habit_sigh = pleasant_habit_sigh

    def __call__(self, habit):
        if habit.get(self.related_habit) and not habit.get(self.pleasant_habit_sigh):
            raise ValidationError(f"Привычка не является приятной")


class PeriodicityValidator:
    """Проверяет, является ли периодичность привычки корректной."""

    def __init__(self, periodicity):
        self.periodicity = periodicity

    def __call__(self, habit):
        if habit.get(self.periodicity) not in range(1, 8):
            raise ValidationError(
                f"Периодичность привычки должна быть в диапазоне от 1 до 7 дней."
            )


class AbsenceValidator:
    """Проверяет отсутствие награды или связанной приятной привычки за выполнение приятной привычки."""

    def __init__(self, reward, related_habit, pleasant_habit_sigh):
        self.reward = reward
        self.related_habit = related_habit
        self.pleasant_habit_sigh = pleasant_habit_sigh

    def __call__(self, habit):
        if (
            habit.get(self.pleasant_habit_sigh)
            and habit.get(self.reward)
            or habit.get(self.related_habit)
        ):
            raise ValidationError(
                f"Приятная привычка не должна иметь вознаграждения или связанную привычку."
            )
