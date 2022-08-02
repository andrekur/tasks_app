from django.contrib import admin

from .models import TaskModel


class TaskAdmin(admin.ModelAdmin):
    fields = (
        'name',
        'descriptions',
        'end_date',
        'owner',
        'task_performers',
    )
    readonly_fields = ('create_date',)


admin.site.register(TaskModel, TaskAdmin)
