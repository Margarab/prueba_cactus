from rest_framework import viewsets, permissions
from users.models import MyUser
from users.serializers import MyUserSerializer


class MyUserViewSet(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer

    def get_permissions(self):
        if self.action in ['list', 'create']:
            self.permission_classes = [IsSuperUser, ]
        elif self.action in ['retrieve', 'update']:
            self.permission_classes = [IsUser]
        return super(self.__class__, self).get_permissions()


class IsSuperUser(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.is_superuser


class IsUser(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user:
            if request.user.is_superuser:
                return True
            else:
                return obj == request.user
        else:
            return False
