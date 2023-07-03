from rest_framework import serializers
from .models import Doctor, Specialty, Availability

class DoctorSerializer(serializers.ModelSerializer):
    # Serializer pour le modèle Doctor

class SpecialtySerializer(serializers.ModelSerializer):
    # Serializer pour le modèle Specialty

class AvailabilitySerializer(serializers.ModelSerializer):
    # Serializer pour le modèle Availability
