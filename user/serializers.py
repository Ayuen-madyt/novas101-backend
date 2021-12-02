from rest_framework import serializers
from dj_rest_auth.serializers import PasswordResetSerializer
from allauth.account.forms import ResetPasswordForm  
from django.contrib.auth.models import User

from .models import Profile

# profile serializer
class SerializerProfile(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


# password reset serializer
class PasswordSerializer(PasswordResetSerializer):
    password_reset_form_class = ResetPasswordForm

# users serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff', 'is_superuser', 'id']