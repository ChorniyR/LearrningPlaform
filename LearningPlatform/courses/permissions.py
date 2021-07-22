from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Checks if user is author of course or not.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
