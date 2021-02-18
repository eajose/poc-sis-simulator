from rest_framework import permissions


class GroupRequiredPermission(permissions.BasePermission):
    group_name = None

    def has_permission(self, request, view):
        groups = request.user.groups.values_list('name', flat=True)
        return self.get_group_name() in groups

    def get_group_name(self):
        assert self.group_name is not None, 'O nome do grupo deve ser definido.'

        return self.group_name


class GrupoApi1(GroupRequiredPermission):
    group_name = 'api'
