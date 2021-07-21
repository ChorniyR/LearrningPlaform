from rest_framework import serializers

from .models import Course


class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['name', 'description', 'details', 'start_date', 'end_date', 'creating_date',]

