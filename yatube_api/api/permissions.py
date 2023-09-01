from rest_framework import permissions


class AuthorOrReadOnlyPermissions(permissions.BasePermission):
    message = "Нельзя редактировать запись другого автора."

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
