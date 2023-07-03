from rest_framework.response import Response
from rest_framework.views import APIView
from django.urls import reverse


class SearchView(APIView):
    def get(self, request, format=None):
        return Response({
            'patients': reverse('patient-search', request=request, format=format),
            'doctors': reverse('doctor-search', request=request, format=format),
            'appointments': reverse('appointment-search', request=request, format=format),
            'medical-records': reverse('medical-record-search', request=request, format=format),
        })

