from django.urls import path, include
from .views import ProfileView, CustomAuthToken, UserViewSet
from rest_framework import routers


router = routers.DefaultRouter()


router.register('profile', ProfileView)
router.register(r'list', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
     path('api-token-auth/', CustomAuthToken.as_view()),
]
