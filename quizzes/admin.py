from django.contrib import admin
from .models import Quiz


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'module', 'passing_score', 'created_at')
    list_filter = ('module__course',)
    search_fields = ('title',)
    readonly_fields = ('created_at',)
