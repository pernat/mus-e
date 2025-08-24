from django.db import models
from django.conf import settings

class Project(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="projects",
        help_text="Project author"
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    cover = models.ImageField(upload_to="project_covers/", blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_archived = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class ProjectSetting(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE, related_name="settings")
    genre = models.CharField(max_length=100, blank=True)
    target_word_count = models.PositiveIntegerField(null=True, blank=True)
    language = models.CharField(max_length=10, default="en")
    status = models.CharField(
        max_length=50,
        choices=[
            ("draft", "Draft"),
            ("in_progress", "In Progress"),
            ("completed", "Completed"),
        ],
        default="draft"
    )

    def __str__(self):
        return f"Settings for {self.project.title}"
