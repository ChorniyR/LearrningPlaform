from django.shortcuts import render
from rest_framework import generics, status
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Step, Lesson
from .serializers import LessonSerializer, StepSerializer


class LessonsDetail(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'


class StepDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, lesson_id, id, format=None):
        step = Step.objects.get(step_id=id)
        step = Step.objects.filter(lesson_id=lesson_id)
        if step:
            serializer = StepSerializer(step, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_204_NO_CONTENT)

