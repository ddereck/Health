from rest_framework import generics
from .models import Doctor, Specialty, Availability
from .serializers import DoctorSerializer, SpecialtySerializer, AvailabilitySerializer

class DoctorCreateView(generics.CreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class DoctorRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    lookup_field = 'id'

class DoctorSearchView(generics.ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    # Logique pour la recherche des médecins

class SpecialtyManagementView(generics.CreateAPIView, generics.UpdateAPIView):
    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer
    lookup_field = 'id'

class AvailabilityManagementView(generics.CreateAPIView, generics.UpdateAPIView):
    queryset = Availability.objects.all()
    serializer_class = AvailabilitySerializer
    lookup_field = 'id'
