from rest_framework import generics, filters
from .serializers import PatientSerializer, DoctorSerializer, AppointmentSerializer, MedicalRecordSerializer
from .models import Patient, Doctor, Appointment, MedicalRecord

class PatientSearchView(generics.ListAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'age', 'sex', 'medical_history']

class DoctorSearchView(generics.ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'specialty']

class AppointmentSearchView(generics.ListAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['date', 'time', 'doctor__name', 'patient__name']

class MedicalRecordSearchView(generics.ListAPIView):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['patient__name', 'consultation_date', 'diagnosis', 'treatment']
