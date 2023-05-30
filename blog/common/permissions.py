# Listing/Common/Permissions.py
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import get_user_model, authenticate

User = get_user_model()


# Check for Django Powerd Admins
class IsSuperAdminOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        index_id = view.kwargs
        id = index_id['id']  # Fetch the ID post for Filter from Any Model, If required.(Currently Not Used)
        try:
            user_scope = request.user.user_scope
        except:
            return False
        if str(user_scope) in ["STAFF", "ADMIN"]:
            return True
        else:
            return False


# Portal Admin permission class - Used for checking is the Auth Uer is a staff / IQAC-NAAC  Cordnator
class IsAdminUser(permissions.BasePermission):

    def has_permission(self, request, view):
        index_id = view.kwargs
      
        try:
            user_scope = request.user.user_scope
            if str(user_scope) in ["IQAC_COD", "NAAC_COD"]:
                return True
            else:
                return False

        except:
            return False



# Allow Get method for All user and Allow Post for Only Authenticated User Roles.
class IsGetOrIsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        # allow all GET requests
        if request.method == 'GET':
            return True

        elif request.user and request.user.is_authenticated:
            try:
                user_scope = request.user.user_scope
                if str(user_scope) in ["IQAC_COD", "STAFF", "NAAC_COD"]:
                    return True
                else:
                    return False
            except:
                return False
        else:
            return False





class IsTeacher(permissions.BasePermission):

    def has_permission(self, request, view):
        index_id = view.kwargs
        try:
            user_scope = request.user.user_scope
            if request.user.is_teacher:
                return True
            else:
                return False
        except:
            return False


# Allow GET method for All user and Allow POST for Only Authenticated User Roles.
class IsGetOrIsAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        # allow all GET requests
        if request.method == 'GET':
            return True

        elif request.user and request.user.is_authenticated:
            return True
        else:
            return False


# Allow POST method for All user and Allow GET for Only Authenticated User Roles.
class IsPostOrIsAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        # allow all POST requests
        if request.method == 'POST':
            return True

        elif request.user and request.user.is_authenticated:
            return True
        else:
            return False