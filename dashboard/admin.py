from django.contrib import admin
from .models import Progress


@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'progress_percentage', 'last_accessed')
    search_fields = ('user__username',)
    readonly_fields = ('last_accessed',)
