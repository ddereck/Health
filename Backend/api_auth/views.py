from django.contrib.auth import authenticate, login
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import PasswordResetConfirmView
from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.cache import never_cache
from rest_framework import generics, permissions, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .models import CustomUser
from .serializers import UserSerializer, UserLoginSerializer, PasswordResetSerializer, PasswordResetConfirmSerializer
from django.contrib.auth.hashers import make_password




class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Hasher le mot de passe
        password = serializer.validated_data['password']
        hashed_password = make_password(password)

        # Créer l'utilisateur avec le mot de passe hashé
        user = CustomUser.objects.create(
            username=serializer.validated_data['username'],
            email=serializer.validated_data['email'],
            password=hashed_password
        )

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class UserLoginAPIView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(request, username=serializer.validated_data['username'], password=serializer.validated_data['password'])
        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

class UserChangePasswordView(PasswordResetConfirmView):
    serializer_class = PasswordResetConfirmSerializer
    success_url = '/password_change_done/'
    template_name = 'change_password.html'

class UserPasswordResetView(generics.GenericAPIView):
    serializer_class = PasswordResetSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        user = CustomUser.objects.filter(email=email).first()
        if user:
            token = default_token_generator.make_token(user)
            uid = user.pk
            return Response({'uid': uid, 'token': token})
        else:
            return Response({'error': 'No user found with this email'}, status=status.HTTP_400_BAD_REQUEST)

sensitive_post_parameters_m = method_decorator(sensitive_post_parameters())

class UserPasswordResetConfirmView(generics.GenericAPIView):
    serializer_class = PasswordResetConfirmSerializer
    permission_classes = [permissions.AllowAny]

    @sensitive_post_parameters_m
    @never_cache
    def dispatch(self, *args, **kwargs):
        return super(UserPasswordResetConfirmView, self).dispatch(*args, **kwargs)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_password = serializer.validated_data['new_password1']
        uid = serializer.validated_data['uid']
        token = serializer.validated_data['token']
        user = CustomUser.objects.get(pk=uid)
        if user is not None and default_token_generator.check_token(user, token):
            user.set_password(new_password)
            user.save()
            return Response({'message': 'Password reset successful'})
        else:
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)

class UserProfileView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
