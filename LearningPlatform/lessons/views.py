from model_bakery import baker
from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Step, Lesson, StepUser
from .serializers import LessonSerializer, StepSerializer, StepUserSerializer, AnswerSerializer
from quizzes.models import Task


class LessonsDetail(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'


class StepDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, lesson_id, id, format=None):
        step = get_object_or_404(Step, lesson_id=lesson_id, id=id)
        if step:
            serializer = StepSerializer(step)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request, lesson_id, id, format=None):
        step = get_object_or_404(Step, lesson_id=lesson_id, id=id)
        answer_serializer = AnswerSerializer(data=request.data, context={'request': request})
        answer_serializer.is_valid(raise_exception=True)
        stepuser = get_object_or_404(StepUser, user=request.user, step=step)
        stepuser_serializer = StepUserSerializer(stepuser)
        return Response(stepuser_serializer.data, status=status.HTTP_201_CREATED)

