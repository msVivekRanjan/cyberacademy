from django.contrib import admin
from .models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'difficulty', 'estimated_duration', 'is_published', 'created_at')
    list_filter = ('difficulty', 'is_published')
    search_fields = ('title', 'short_description')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('is_published',)
    readonly_fields = ('created_at', 'updated_at')
