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
    ViewSet for viewing, editing and enrolling courses.
    """
    queryset = Course.objects.all()
    serializer_class = CoursesSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly, StuffCreatePermission]

    @action(methods=['GET'], detail=False)
    def my(self, request, pk=None):
        """
        This action views all courses that user have enrolled.
        """
        course_user = CourseUser.objects.filter(user=request.user)
        if course_user:
            serializer = CourseUserSerializer(course_user, many=True, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(methods=['POST'], detail=True, serializer_class=CourseUserSerializer,
            permission_classes=[permissions.IsAuthenticated])
    def enroll(self, request, pk=None):
        """
        By this action user can enroll course.
        If user had already enrolled on any course, action will just add the course in CourseUser table,
        but if user have never been enrolled on any courses, it will create new instance in CourseUser table.
        """
        course = Course.objects.get(id=pk)
        user = request.user
        try:
            instance = CourseUser.objects.get(user=request.user)
        except CourseUser.DoesNotExist:
            instance = CourseUser.objects.create()
            instance.user.add(user)
            instance.course.add(course)
        else:
            instance.course.add(course)

        serializer = CourseUserSerializer(instance)
        return Response(serializer.data)
