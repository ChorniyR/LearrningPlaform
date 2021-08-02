from model_bakery.baker import make
from rest_framework import viewsets, status
from rest_framework import permissions
from rest_framework.decorators import action, api_view
from rest_framework.response import Response

from .models import Course, CourseUser
from .serializers import CoursesSerializer, CourseUserSerializer
from .permissions import IsAuthorOrReadOnly, StuffCreatePermission


class CoursesViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing end editing courses
    """
    queryset = Course.objects.all()
    serializer_class = CoursesSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly, StuffCreatePermission]

    @action(methods=['GET'], detail=False)
    def my(self, request, pk=None):
        user_courses = CourseUser.objects.filter(user=request.user)
        if user_courses:
            serializer = CourseUserSerializer(user_courses, many=True, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(methods=['POST'], detail=True, serializer_class=CourseUserSerializer,
            permission_classes=[permissions.IsAuthenticated])
    def add(self, request, pk=None):
        if pk:
            course = Course.objects.get(id=pk)
            user = request.user
            instance = CourseUser.objects.get(user=request.user)

            if instance:
                instance.course.add(course)
            else:
                instance = CourseUser.objects.create()
                instance.user.add(user)
                instance.course.add(course)

            serializer = CourseUserSerializer(instance)
            return Response(serializer.data)
        return Response(status=status.HTTP_204_NO_CONTENT)