from rest_framework import serializers
from core.models import Recipe
from core.serializers.user import UserSerializer



class RecipeDetailSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    class Meta:
        model=Recipe
        fields="__all__"

class RecipeSerializer(serializers.ModelSerializer):
      class Meta:
        model=Recipe
        fields="__all__"
