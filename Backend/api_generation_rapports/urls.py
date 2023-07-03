from django.urls import path, include
from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    # Autres URLs de l'application
    
    # Inclure les URLs de l'API
    path('api/', include('api_generation_rapports.urls')),
]
