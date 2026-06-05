from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """Extended profile linked to Django's built-in User."""

    LEVEL_CHOICES = [
        ('rookie', 'Rookie'),
        ('analyst', 'Analyst'),
        ('specialist', 'Specialist'),
        ('expert', 'Expert'),
        ('elite', 'Elite'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_image = models.ImageField(upload_to='profiles/', blank=True, null=True)
    bio = models.TextField(blank=True)
    xp_points = models.PositiveIntegerField(default=0)
    streak = models.PositiveIntegerField(default=0)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default='rookie')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'

    def __str__(self):
        return f"{self.user.username} — {self.get_level_display()}"
