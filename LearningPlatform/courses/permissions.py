from rest_framework import permissions


class IsCourseAuthor(permissions.BasePermission):
    """
    Checks if user is author of course or not.
    """
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
