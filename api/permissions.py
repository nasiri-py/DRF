from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsSuperUser(BasePermission):
    """
    Allow access only to superuser
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)


class IsStaffOrReadOnly(BasePermission):
    """
    The request is staff as a user, or is a read-only request.
    """

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and request.user.is_staff
        )


class IsAuthorOrReadOnly(BasePermission):
    """
    The request is author as a user, or is a read-only request.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in SAFE_METHODS:
            return True

        # Instance must have an attribute named `author`.
        return bool(
            request.user and request.user.is_superuser
            or
            obj.author == request.user
        )


class IsSuperUserOrStaffReadOnly(BasePermission):
    """
    The request is superuser as a user, or is a read-only by staff as a user.
    """

    def has_permission(self, request, view):
        """
        Read permissions are allowed to staff as a user,
        so we'll always allow GET, HEAD or OPTIONS requests.
        Instance must the request is superuser as a user.
        """

        return bool(
            request.method in SAFE_METHODS and (request.user and request.user.is_staff)
            or
            request.user and request.user.is_superuser
        )
