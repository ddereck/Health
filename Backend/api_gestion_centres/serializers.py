from rest_framework import serializers
from .models import Centre, Abonnement, Message
from django.contrib.auth.models import User

class AbonnementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Abonnement
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class CentreSerializer(serializers.ModelSerializer):
    abonnements = AbonnementSerializer(many=True, read_only=True)
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Centre
        fields = '__all__'




# class CentreSerializer(serializers.ModelSerializer):
#     administrateur = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

#     class Meta:
#         model = Centre
#         fields = ['id', 'nom', 'adresse', 'administrateur']
