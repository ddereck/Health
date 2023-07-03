from rest_framework import serializers
from .models import Invoice, Payment, InsuranceReimbursement

class InvoiceSerializer(serializers.ModelSerializer):
    # Serializer pour le modèle Invoice

class PaymentSerializer(serializers.ModelSerializer):
    # Serializer pour le modèle Payment

class InsuranceReimbursementSerializer(serializers.ModelSerializer):
    # Serializer pour le modèle InsuranceReimbursement
