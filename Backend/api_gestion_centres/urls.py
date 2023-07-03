from django.urls import path
from . import views

app_name = 'api_gestion_centres'

urlpatterns = [
    path('centres/', views.CentreListCreateAPIView.as_view(), name='centre-list-create'),
    path('centres/<int:pk>/', views.CentreRetrieveUpdateDestroyAPIView.as_view(), name='centre-retrieve-update-destroy'),
     path('centres/<int:pk>/abonnements/', views.AbonnementListAPIView.as_view(), name='centre-abonnements-list'),
    path('centres/<int:pk>/messages/', views.MessageListAPIView.as_view(), name='centre-messages-list'),
]
