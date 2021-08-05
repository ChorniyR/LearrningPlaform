from rest_framework import serializers

from .models import Lesson, Step, StepUser
from quizzes.serializers import TestSerializer
from quizzes.serializers import TaskSerializer


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
        fields = ['passed', 'score', 'user', 'step', 'feedback',]


class AnswerSerializer(serializers.Serializer):
    test = TestSerializer()
    step = StepSerializer(read_only=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        if validated_data['test'].is_passed():
            step_user = StepUser.objects.create(passed=True,
                                                score=36,
                                                user=self.context['request'].user,
                                                step=validated_data['step'],
                                                feedback="You are good!!")





