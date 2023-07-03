from rest_framework.permissions import BasePermission

class IsDoctor(BasePermission):
    def has_permission(self, request, view):
        # Vérifier si l'utilisateur est un médecin
        # Retourner True s'il est médecin, False sinon
        return request.user.is_doctor

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        # Vérifier si l'utilisateur est un administrateur
        # Retourner True s'il est administrateur, False sinon
        return request.user.is_admin
