from rest_framework import permissions


class AuthorOrReadOnlyPermissions(permissions.BasePermission):
    message = "Нельзя редактировать запись другого автора."

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user)
