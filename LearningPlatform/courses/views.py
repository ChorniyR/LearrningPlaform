from model_bakery.baker import make
from rest_framework import viewsets, status
from rest_framework import permissions
from rest_framework.decorators import action
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
        """
        course = Course.objects.get(id=pk)
        user = request.user

        course_user = CourseUser.add_course_to_user(user, course)
        serializer = CourseUserSerializer(course_user)
        return Response(serializer.data)
