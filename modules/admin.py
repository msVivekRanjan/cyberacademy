from django.contrib import admin
from .models import Module


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'order', 'created_at')
    list_filter = ('course',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('course', 'order')
    readonly_fields = ('created_at', 'updated_at')
