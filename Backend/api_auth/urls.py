from django.urls import path
from . import views

app_name = 'api_auth'

urlpatterns = [
    path('users/', views.UserListCreateAPIView.as_view(), name='user-list-create'),
    path('users/login/', views.UserLoginAPIView.as_view(), name='user-login'),
    path('users/password/reset/', views.UserPasswordResetView.as_view(), name='password-reset'),
    path('users/password/reset/confirm/', views.UserPasswordResetConfirmView.as_view(), name='password-reset-confirm'),
    path('users/change_password/', views.UserChangePasswordView.as_view(), name='change-password'),
    path('users/profile/', views.UserProfileView.as_view(), name='user-profile'),
]
