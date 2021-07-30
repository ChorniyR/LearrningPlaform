from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Checks if user is author of course or not.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


class StuffCreatePermission(permissions.BasePermission):
    """
    Checks if user is stuff allows to POST method.
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.method in ['POST']:
            return request.user.is_staff
