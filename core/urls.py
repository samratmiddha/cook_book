
from django.urls import path, include
from rest_framework import routers

from core.views import UserViewSet,RecipeViewset,logout_user,login_user,whoami,sign_up

router = routers.SimpleRouter()

router.register(r'users', UserViewSet)
router.register(r'recipes', RecipeViewset)


urlpatterns = [
    path('', include(router.urls)),
    path('whoami/', whoami),
    path('login/', login_user),
    path('logout/',logout_user),
    path('sign_up/',sign_up)
]


