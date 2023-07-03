from django.urls import path
from .views import (
    DoctorCreateView,
    DoctorRetrieveUpdateDeleteView,
    DoctorSearchView,
    SpecialtyManagementView,
    AvailabilityManagementView,
)

urlpatterns = [
    path('doctors/', DoctorCreateView.as_view(), name='doctor-create'),
    path('doctors/<int:id>/', DoctorRetrieveUpdateDeleteView.as_view(), name='doctor-detail'),
    path('doctors/search/', DoctorSearchView.as_view(), name='doctor-search'),
    path('specialties/', SpecialtyManagementView.as_view(), name='specialty-management'),
    path('availability/', AvailabilityManagementView.as_view(), name='availability-management'),
]
