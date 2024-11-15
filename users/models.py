from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None
    email = models.EmailField(
        verbose_name="email", unique=True, help_text="введите почту", **NULLABLE
    )
    phone = models.CharField(
        max_length=35,
        verbose_name="номер телефона",
        help_text="введите номер",
        **NULLABLE
    )
    city = models.CharField(
        max_length=35, verbose_name="город", help_text="укажите город", **NULLABLE
    )
    avatar = models.ImageField(
        upload_to="users/avatars",
        verbose_name="аватар",
        help_text="выберите изображение",
        **NULLABLE
    )
    tg_chat_id = models.CharField(
        max_length=35, verbose_name="telegram chat id", help_text="telegram чат id"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"
