from rest_framework import permissions

class CanRetrieveRecipe(permissions.BasePermission):
    def has_object_permission(self, request,view, obj):
        return obj.is_public == True or obj.owner.id==request.user.id
    

class IsRecipeOwner(permissions.BasePermission):
    def has_object_permission(self, request,view,obj):
       
        return obj.owner.id == request.user.id
    
class IsSelf(permissions.BasePermission):
    def has_object_permission(self, request,view,obj):
        return obj.id == request.user.id
        
        