from rest_framework import serializers

from .models import Test, Task, TaskCase


class TestSerializer(serializers.ModelSerializer):
    tasks = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='tasks-detail'
    )

    class Meta:
        model = Test
        fields = ['description', 'passed', 'step', 'tasks']


class TaskSerializer(serializers.ModelSerializer):
    cases = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='cases-detail'
    )

    class Meta:
        model = Task
        fields = ['definition', 'cases', 'passed']


class TaskCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskCase
        fields = ['definition', 'selected']
