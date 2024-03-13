from rest_framework import viewsets
from core.models import User
from core.serializers import UserSerializer,UserFavouritesSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from django.contrib.auth import login,authenticate,logout
from core.permissions import IsSelf
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST,HTTP_401_UNAUTHORIZED,HTTP_201_CREATED,HTTP_500_INTERNAL_SERVER_ERROR



class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    permission_classes=[IsAuthenticated,IsSelf]

    def get_serializer_class(self):
        if self.action == "list":
            return UserSerializer
        else:
            return UserFavouritesSerializer
        


@api_view(['POST'])
@permission_classes([])
def login_user(request):
    username=request.data['username']
    password=request.data['password']
    remember_me=request.data['remember_me']
    user = authenticate(username=username,password=password)
    if user is not None:
        if not remember_me:
                request.session.set_expiry(60*60)
        login(request,user)
        serializer=UserSerializer(user)
        return Response(serializer.data,status=HTTP_200_OK)
    else:
         return Response({"message":"The entered username or password is wrong"},status=HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
@permission_classes([])
def whoami(request):
    if request.user.is_authenticated:
        user_data=UserFavouritesSerializer(request.user).data
        return Response(user_data,status=HTTP_200_OK)
    return Response({'message':'User not logged in '},status=HTTP_401_UNAUTHORIZED)


@api_view(('GET',))
def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return Response({'message':"user logged out Successfully"},status=HTTP_200_OK)
    return Response({'message':"user already logged out"},status=HTTP_200_OK)
    
@api_view(['POST'])
@permission_classes([])
def sign_up(request):
    email=request.data.get('email')
    username=request.data.get('username')
    password=request.data.get('password')
    first_name=request.data.get('first_name')
    last_name=request.data.get('last_name')

    
    if not username and not password:
        return Response({"message":"Username/Password not provided"},status=HTTP_400_BAD_REQUEST)
    
    if not first_name :
        return Response({"message":"Name not provided"},status=HTTP_400_BAD_REQUEST)
    
    try:
      user=User.objects.get(username=username)
      return Response({"message":"User already exists"},status=HTTP_400_BAD_REQUEST)
    except User.DoesNotExist:
        try:
            user=User.objects.create(username=username,first_name=first_name, last_name=last_name,email=email)
            user.set_password(password)
            user.save()
            login(request, user)
            serializer=UserSerializer(user)
            return Response(serializer.data,status=HTTP_201_CREATED)
        except:
            return Response({"message":"Error while creating user"},status=HTTP_500_INTERNAL_SERVER_ERROR)



        
        