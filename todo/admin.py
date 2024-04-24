from django.contrib import admin

from todo.models import Tag, Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["created_at", "deadline", "tag"]
    list_filter = ["created_at", "deadline"]
    search_fields = ["content", ]


admin.site.register(Tag)
