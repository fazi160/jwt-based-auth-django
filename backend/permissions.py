from rest_framework import permissions
from django.contrib.auth import get_user_model


User = get_user_model()

class AdminPermission(permissions.BasePermission):
    """
    Custom permission to only allow access if the user is an admin or superuser.
    """

    def has_permission(self, request, view):
        return request.user.user_type == 'admin' or request.user.is_superuser


class AuthorPermission(permissions.BasePermission):
    """
    Custom permission to only allow access if the user is an author and is permitted.
    """

    def has_permission(self, request, view):
        return request.user.user_type == 'author' and request.user.is_permitted


class UserPermission(permissions.BasePermission):
    """
    Custom permission to only allow access if the user is a regular user.
    """

    def has_permission(self, request, view):
        return request.user.user_type == 'user'


class AuthorEditPermission(permissions.BasePermission):
    """
    Custom permission to only allow the author of the blog to edit or change it.
    """

    def has_object_permission(self, request, view, obj):
        # obj is an instance of the Blog model
        return obj.blogger == request.user
