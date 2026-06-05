from django.db import models
from modules.models import Module


class Quiz(models.Model):
    """Assessment quiz attached to a module."""

    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='quizzes')
    title = models.CharField(max_length=200)
    passing_score = models.PositiveIntegerField(default=70, help_text='Minimum % to pass')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Quiz'
        verbose_name_plural = 'Quizzes'

    def __str__(self):
        return f"{self.module.title} — {self.title}"
