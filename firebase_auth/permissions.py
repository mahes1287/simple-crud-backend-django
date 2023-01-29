from rest_framework import permissions


class LoginNeeded(permissions.BasePermission):
    message = "please login"

    def has_permission(self, request, view):
        return request.user.is_authenticated


class AllowAll(permissions.BasePermission):
    message = "Success"

    def has_permission(self, request, view):
        print("jhdjfdsfdsfsdh")
        # if request.method in permissions.SAFE_METHODS:
        return True

    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    # def has_object_permission(self, request, view, obj):
    #     print("jhdjfdsfdsfsdh2222222222222222222222222222")
    #     # Read permissions are allowed to any request,
    #     # so we'll always allow GET, HEAD or OPTIONS requests.
    #     if request.method in permissions.SAFE_METHODS:
    #         return True
