from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Course
from .serializers import CoursesSerializer


class CoursesViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing end editing courses
    """
    queryset = Course.objects.all()
    serializer_class = CoursesSerializer


class CourseDetail(APIView):
    """
    Retrieve, update or delete a course instance.
    """

    def get(self, request, pk, format=None):
        course = get_object_or_404(Course, pk=pk)
        serializer = CoursesSerializer(course)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        course = get_object_or_404(Course, pk=pk)
        serializer = CoursesSerializer(course, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        course = get_object_or_404(pk)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
