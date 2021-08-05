from rest_framework import serializers

from .models import Test, Task, TaskCase


class TaskCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskCase
        fields = ['id', 'definition', 'selected']


class TaskSerializer(serializers.ModelSerializer):
    cases = TaskCaseSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'definition', 'cases', 'passed']


class TestSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)


    class Meta:
        model = Test
        fields = ['id', 'description', 'passed', 'step', 'tasks']
