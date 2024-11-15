from django.contrib import admin

from habits.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = (
        "owner",
        "action",
        "is_published",
    )
    list_filter = ("owner",)
    search_fields = ("action",)
