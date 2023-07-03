from rest_framework import serializers
from Backend.api_auth.models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email', 'first_name', 'last_name']

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'}, trim_whitespace=False)

class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()

class PasswordResetConfirmSerializer(serializers.Serializer):
    new_password1 = serializers.CharField(style={'input_type': 'password'}, trim_whitespace=False)
    new_password2 = serializers.CharField(style={'input_type': 'password'}, trim_whitespace=False)
    uid = serializers.CharField()
    token = serializers.CharField()
