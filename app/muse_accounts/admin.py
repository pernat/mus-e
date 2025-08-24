
# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """Админ-панель для кастомной модели пользователя."""

    # Какие поля отображать в списке пользователей
    list_display = (
        "username", "email", "display_name",
        "preferred_language", "theme", "is_staff"
    )
    list_filter = ("preferred_language", "theme", "is_staff", "is_superuser")
    search_fields = ("username", "email", "display_name")

    # Поля, которые будут редактироваться
    fieldsets = UserAdmin.fieldsets + (
        ("Дополнительные данные", {
            "fields": (
                "display_name",
                "avatar",
                "bio",
                "preferred_language",
                "theme",
            )
        }),
    )

    # Поля для формы создания нового пользователя
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Дополнительные данные", {
            "classes": ("wide",),
            "fields": (
                "display_name",
                "avatar",
                "bio",
                "preferred_language",
                "theme",
            ),
        }),
    )

    def avatar_tag(self, obj):
        if obj.avatar:
            return format_html('<img src="{}" style="width:40px;height:40px;border-radius:50%"/>', obj.avatar.url)
        return "—"
    avatar_tag.short_description = "Avatar"

    list_display = (
        "username", "email", "display_name",
        "preferred_language", "theme", "avatar_tag", "is_staff"
    )

