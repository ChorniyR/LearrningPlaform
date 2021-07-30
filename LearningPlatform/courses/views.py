from rest_framework import viewsets
from rest_framework import permissions


from .models import Course
from .serializers import CoursesSerializer
from .permissions import IsAuthorOrReadOnly, StuffCreatePermission


class CoursesViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing end editing courses
    """
    queryset = Course.objects.all()
    serializer_class = CoursesSerializer
    permission_classes = [permissions.IsAuthenticated, StuffCreatePermission, IsAuthorOrReadOnly]

