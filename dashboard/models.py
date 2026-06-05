from django.db import models
from django.contrib.auth.models import User
from modules.models import Module
from quizzes.models import Quiz


class Progress(models.Model):
    """Tracks a user's learning progress across modules and quizzes."""

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='progress')
    completed_modules = models.ManyToManyField(Module, blank=True, related_name='completions')
    completed_quizzes = models.ManyToManyField(Quiz, blank=True, related_name='completions')
    progress_percentage = models.FloatField(default=0.0)
    last_accessed = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Progress'
        verbose_name_plural = 'Progress Records'

    def __str__(self):
        return f"{self.user.username} — {self.progress_percentage:.1f}%"
