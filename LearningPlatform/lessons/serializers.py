from quizzes.models import Test
from rest_framework import serializers

from .models import Lesson, Step, StepUser
from quizzes.serializers import TestSerializer


class StepSerializer(serializers.ModelSerializer):
    test = TestSerializer(read_only=True)

    class Meta:
        model = Step
        fields = ['likes', 'number', 'dislikes', 'title', 'test']

    def create(self, validated_data):
        return Step(**validated_data)

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['title']


class StepUserSerializer(serializers.ModelSerializer):
    step = StepSerializer(many=True, read_only=True)

    class Meta:
        model = StepUser
        fields = ['passed', 'score', 'user', 'step', 'feedback', ]


class UserAnswerSerializer(serializers.Serializer):
    test = TestSerializer()
    step = StepSerializer(read_only=True)

    def update(self, instance, validated_data):

        return super().update(instance, validated_data)

    def create(self, validated_data):
        return Test(**self.validated_data)
