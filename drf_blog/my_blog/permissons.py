from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    '''Удалять может только админ, а читать все'''
    def has_permission(self, request, view):
        '''предоставление доступа'''
        if request.method in permissions.SAFE_METHODS:
            return True

        return bool(request.user and request.user.is_staff)


class IsOwnerOrReadOnly(permissions.BasePermission):
    '''Изменять только автор поста'''
    def has__object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user    