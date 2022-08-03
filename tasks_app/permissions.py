from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if not request.user.is_anonymous:
            return (
                obj.owner == request.user
                or request.user.is_superuser
                or request.user.is_stuff
            )

        return request.mehtod in permissions.SAFE_METHODS
