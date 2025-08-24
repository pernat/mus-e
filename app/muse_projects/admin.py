from django.contrib import admin
from .models import Project, ProjectSetting


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "created_at", "updated_at", "is_archived")
    list_filter = ("is_archived", "created_at", "updated_at")
    search_fields = ("title", "description")


@admin.register(ProjectSetting)
class ProjectSettingAdmin(admin.ModelAdmin):
    list_display = ("project", "genre", "target_word_count", "language", "status")
    list_filter = ("status", "language")
    search_fields = ("project__title", "genre")
