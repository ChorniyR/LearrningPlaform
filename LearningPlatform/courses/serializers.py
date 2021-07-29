from rest_framework import serializers

from .models import Course


class CoursesSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Course
        fields = ['name', 'description', 'details', 'start_date', 'end_date', 'creating_date', 'author']

    def validate(self, attrs):
        if attrs['start_date'] > attrs['end_date']:
            raise serializers.ValidationError("Start date should be as early as end_date")
        return attrs
