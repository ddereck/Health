from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Centre, Abonnement, Message
from .serializers import CentreSerializer, AbonnementSerializer, MessageSerializer

class CentreListCreateAPIView(generics.ListCreateAPIView):
    queryset = Centre.objects.all()
    serializer_class = CentreSerializer

    @action(detail=True, methods=['PUT'])
    def update_administrateur(self, request, pk=None):
        centre = self.get_object()
        administrateur_id = request.data.get('administrateur')
        administrateur = User.objects.get(id=administrateur_id)
        centre.administrateur = administrateur
        centre.save()
        serializer = self.get_serializer(centre)
        return Response(serializer.data)


class CentreRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Centre.objects.all()
    serializer_class = CentreSerializer


class AbonnementListAPIView(generics.ListAPIView):
    queryset = Abonnement.objects.all()
    serializer_class = AbonnementSerializer


class MessageListAPIView(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
