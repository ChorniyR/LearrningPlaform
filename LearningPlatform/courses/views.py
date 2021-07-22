from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Course
from .serializers import CoursesSerializer
from .permissions import IsAuthorOrReadOnly


class CoursesViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing end editing courses
    """
    queryset = Course.objects.all()
    serializer_class = CoursesSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]
