from rest_framework import serializers

from .models import Course, CourseUser
from lessons.models import Lesson


class CoursesSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Course
        fields = ['name', 'description', 'details', 'start_date', 'end_date', 'creating_at', 'author']

    def validate(self, attrs):
        if attrs['start_date'] > attrs['end_date']:
            raise serializers.ValidationError("Start date should be as early as end_date")
        return attrs


class CourseUserSerializer(serializers.ModelSerializer):
    course = CoursesSerializer(many=True, read_only=True)

    class Meta:
        model = CourseUser
        fields = ['course', 'passed', 'user']
        extra_kwargs = {
            'user': {'read_only': True},
            'passed': {'read_only': True},
        }
