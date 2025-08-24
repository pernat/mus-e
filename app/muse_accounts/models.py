from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Кастомная модель пользователя для проекта Muse.
    Наследуется от AbstractUser → сохраняет совместимость с Django.
    """

    # Дополнительные поля
    display_name = models.CharField(
        max_length=150,
        blank=True,
        help_text="Публичное имя автора (может отличаться от username)."
    )
    avatar = models.ImageField(
        upload_to="avatars/",
        blank=True,
        null=True,
        help_text="Аватар пользователя."
    )
    bio = models.TextField(
        blank=True,
        help_text="Короткая биография или заметка об авторе."
    )
    preferred_language = models.CharField(
        max_length=10,
        choices=[("en", "English"), ("ru", "Русский")],
        default="en",
        help_text="Предпочитаемый язык интерфейса."
    )
    theme = models.CharField(
        max_length=20,
        choices=[("light", "Light"), ("dark", "Dark"), ("zen", "Zen Mode")],
        default="zen",
        help_text="Выбранная тема интерфейса."
    )

    def __str__(self):
        return self.display_name or self.username
