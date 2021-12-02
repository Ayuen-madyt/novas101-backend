from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import SerializerProfile,  UserSerializer
from .models import Profile

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

# where we get the user profile, it is created automatically in signals.py file upon registering
class ProfileView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Profile.objects.all()
    serializer_class = SerializerProfile

# where we obtain user token and user details upon login
class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'username': user.username,
            'is_staff': user.is_staff,
            'is_superuser':user.is_superuser
        })

# users list
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer