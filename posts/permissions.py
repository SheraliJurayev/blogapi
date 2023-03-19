from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        #read-only permissions
        if request.method in permissions.SAFE_METHODS:
            return True

        # write-only permissions for only posts authors
        return obj.author == request.user
