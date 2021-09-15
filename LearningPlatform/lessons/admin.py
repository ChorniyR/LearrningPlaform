from django.contrib import admin

from .models import Lesson, Step, StepUser


admin.site.register(Lesson)
admin.site.register(Step)
admin.site.register(StepUser)