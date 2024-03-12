from rest_framework import viewsets
from core.models import Recipe
from django.db.models import Q
from core.serializers import RecipeSerializer,RecipeDetailSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.decorators import action,permission_classes
from rest_framework import filters




class RecipeViewset(viewsets.ModelViewSet):
    queryset=Recipe.objects.all()
    permission_classes=[]
    filter_backends = [filters.SearchFilter]
    search_fields = ['titile', 'ingredients']

    def get_serializer_class(self):
        if self.action in ["list","retrieve"]:
            return RecipeDetailSerializer
        else:
            return RecipeSerializer
        
    def list(self,request):
        public_recipes=Recipe.objects.filter(is_public=True)
        user_private_recipes=Recipe.objects.filter(is_public=False,owner=self.request.user.id)
        combined_queryset=public_recipes.union(user_private_recipes)
        serializer=RecipeDetailSerializer(combined_queryset,many=True)
        return Response(serializer.data,status=HTTP_200_OK  )


    
    @action(methods=['GET'],detail=False,url_name='search/')
    def search(self,request):
        value = request.GET.get('value')
        public_recipes = Recipe.objects.filter(is_public=True)

        user_private_recipes = Recipe.objects.filter(is_public=False, owner=request.user.id)

        if value:
            public_recipes = public_recipes.filter(
            Q(title__icontains=value) | Q(ingredients__icontains=value)
            )
            user_private_recipes = user_private_recipes.filter(
            Q(title__icontains=value) | Q(ingredients__icontains=value)
            )
        

        combined_queryset = public_recipes.union(user_private_recipes)
        serializer=RecipeDetailSerializer(combined_queryset,many=True)
        return Response(serializer.data,status=HTTP_200_OK  )
        


    
    @action(methods=['POST'],detail=False,url_name='get_user_recipes/')
    def get_user_recipes(self,request):
        user = request.GET.get('user')
        user_recipes=Recipe.objects.filter(owner=user)
        serializer=self.get_serializer_class()(user_recipes,many=True)
        return Response(serializer.data, status=HTTP_200_OK)

        
        
    

    
    

        
        



