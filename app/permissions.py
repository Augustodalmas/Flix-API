from rest_framework import permissions

class globalPermissions(permissions.BasePermission):

    def has_permission(self, request, view): 
        codename = self._get_codename(method=request.method, view=view)
        if not codename:
            return None
        return request.user.has_perm(codename)
    

    def _get_codename(self, method, view):
        try:
            model_name = view.queryset.model._meta.model_name
            app_name = view.queryset.model._meta.app_label
            action = self._get_action(method)
            return f'{model_name}.{action}_{app_name}'
        except AttributeError:
            return None
        

    def _get_action(self, method):
        method_Actions = {
            "GET": 'view',
            "OPTIONS": 'view',
            "HEAD": 'view',
            "POST": 'add',
            "PATCH": 'change',
            "PUT": 'change',
            "DELETE": 'delete',
        }
        return method_Actions.get(method, "")