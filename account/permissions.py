from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsBoss(BasePermission):
    message = 'you are not BOSS and do not have permission, silly!...'
    def has_permission(self, request, view):
        print(request.user.profile.role)
        if request.user.profile.role == 'BOSS':
            return True
        else:
            return False

class IsManager(BasePermission):
    message = 'you are not MANAGER and do not have permission, silly!...'
    def has_permission(self, request, view):
        print(request.user.profile.role)
        if request.user.profile.role == 'MANAGER':
            return True
        else:
            return False

class IsSuperVisor(BasePermission):
    message = 'you are not SUPERVISOR and do not have permission, silly!...'
    def has_permission(self, request, view):
        print(request.user.profile.role)
        if request.user.profile.role == 'SUPERVISOR':
            return True
        else:
            return False

class IsStaff(BasePermission):
    message = 'you are not STAFF and do not have permission, silly!...'
    def has_permission(self, request, view):
        print(request.user.profile.role)
        if request.user.profile.role == 'STAFF':
            return True
        else:
            return False