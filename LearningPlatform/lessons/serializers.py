from rest_framework import serializers

from .models import Lesson, Step, StepUser
from quizzes.serializers import TestSerializer


class StepSerializer(serializers.ModelSerializer):
    test = TestSerializer(read_only=True)

    class Meta:
        model = Step
        fields = ['likes', 'number', 'dislikes', 'title', 'test']


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['title']


class StepUserSerializer(serializers.ModelSerializer):
    step = StepSerializer(many=True, read_only=True)

    class Meta:
        model = StepUser
        fields = ['passed', 'score', 'user', ]
