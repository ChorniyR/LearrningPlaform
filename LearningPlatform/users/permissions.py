from rest_framework import permissions


class IsStuffOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.method in ['POST', 'PUT'] and request.user.is_stuff
