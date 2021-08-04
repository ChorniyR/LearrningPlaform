from django.contrib import admin

from .models import Task, TaskCase, Test

admin.site.register(Test)
admin.site.register(TaskCase)
admin.site.register(Task)