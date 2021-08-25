import copy
from quizzes.models import Task, Test, TaskCase

from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Step, Lesson
from .serializers import LessonSerializer, StepSerializer, UserAnswerSerializer


class LessonsDetail(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'


class StepDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, lesson_id, id, format=None):
        """
        By this view user can see the detail of current step.
        :lesson_id - id of current course.
        :id - id of current step.
        """
        step = get_object_or_404(Step, lesson_id=lesson_id, id=id)
        if step:
            serializer = StepSerializer(step)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request, lesson_id, id, format=None):
        tasks = parse_tasks(request.data)
        for task in tasks:
            cases = TaskCase.get_by_task_id(task.id)
            posted_cases = parse_cases(request.data)
            task.passed = Task.is_passed(cases, posted_cases)
        print(tasks[0].passed)
        

def parse_cases(data):
    cases = []
    for task in data['test']['tasks']:
        for kwargs in task.get('cases'):
            del kwargs['task']
            cases.append(TaskCase(**kwargs))
    return cases

def parse_tasks(data):
    test = copy.deepcopy(data['test'])
    tasks = []
    for kwargs in test.get('tasks'):
        del kwargs['cases']
        tasks.append(Task(**kwargs))
    return tasks