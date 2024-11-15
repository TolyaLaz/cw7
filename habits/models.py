from datetime import timedelta

from django.db import models

from config import settings

NULLABLE = {"blank": True, "null": True}


class Habit(models.Model):
    owner = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="владелец",
        **NULLABLE,
    )
    place = models.CharField(
        max_length=100,
        verbose_name="место выполнения привычки",
        help_text="где нужно выполнять привычку",
    )
    time = models.DateTimeField(
        verbose_name="начало выполнения привычки",
        help_text="выберите дату и время начала",
    )
    action = models.TextField(
        verbose_name="что нужно сделать",
        help_text="опишите действие, которое нужно сделать",
    )
    pleasant_habit_sign = models.BooleanField(
        verbose_name="признак приятной привычки",
        help_text="является ли привычка приятной",
        default=False,
    )
    related_habit = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        verbose_name="связанная привычка",
        help_text="укажите связанную привычку",
        **NULLABLE,
    )
    periodicity = models.SmallIntegerField(
        default=1,
        verbose_name="периодичность",
        help_text="сколько раз в неделю: от 1 до 7",
    )
    reward = models.CharField(
        max_length=150,
        verbose_name="награда за выполнение",
        help_text="опишите награду за выполнение привычки",
        **NULLABLE,
    )
    duration = models.DurationField(
        verbose_name="продолжительность выполнения",
        help_text="укажите как долго нужно выполнять привычку",
        default=timedelta(minutes=2),
    )
    is_published = models.BooleanField(
        verbose_name="признак публикации",
        help_text="опубликовать привычку",
        default=True,
    )

    def __str__(self):
        return f"{self.owner} будет {self.action} в {self.time} в {self.place}"

    class Meta:
        verbose_name = "привычка"
        verbose_name_plural = "привычки"
