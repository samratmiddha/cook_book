from rest_framework import serializers
from core.models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["id","username","first_name","last_name","email"]

class UserFavouritesSerializer(serializers.ModelSerializer):
     class Meta:
        model=User
        fields=fields=["id","username","first_name","last_name","email","favourites"]
    