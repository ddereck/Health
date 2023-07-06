from django.urls import path, reverse
from .views import SearchView, PatientSearchView, DoctorSearchView, AppointmentSearchView, MedicalRecordSearchView

urlpatterns = [
    path('search/', SearchView.as_view(), name='search'),
    path('search/patients/', PatientSearchView.as_view(), name='patient-search'),
    path('search/doctors/', DoctorSearchView.as_view(), name='doctor-search'),
    path('search/appointments/', AppointmentSearchView.as_view(), name='appointment-search'),
    path('search/medical-records/', MedicalRecordSearchView.as_view(), name='medical-record-search'),
]
