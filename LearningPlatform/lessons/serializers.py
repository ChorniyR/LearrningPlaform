from rest_framework import serializers

from .models import Lesson, Step, StepUser
from quizzes.serializers import TestSerializer
from reading_materials.serializers import ReadingMaterialSerializer


class StepSerializerReadOnly(serializers.ModelSerializer):
    """
    This serializer is used to viewing title and number of step.
    """

    class Meta:
        model = Step
        fields = ['number', 'title']
        extra_kwargs = {
            'number': {'read_only': True},
            'title': {'read_only': True}
        }


class StepSerializer(serializers.ModelSerializer):
    test = TestSerializer(read_only=True)
    reading_material = ReadingMaterialSerializer(read_only=True)

    class Meta:
        model = Step
        fields = ['id', 'likes', 'number', 'dislikes', 'title', 'test', 'reading_material']

    def create(self, validated_data):
        return Step(**validated_data)


class LessonSerializer(serializers.ModelSerializer):
    steps = StepSerializerReadOnly(many=True, read_only=True)

    class Meta:
        model = Lesson
        fields = ['title', 'steps']


class StepUserSerializer(serializers.ModelSerializer):
    step = StepSerializer(many=True, read_only=True)

    class Meta:
        model = StepUser
        fields = ['id', 'passed', 'user', 'step', 'feedback', 'score']
