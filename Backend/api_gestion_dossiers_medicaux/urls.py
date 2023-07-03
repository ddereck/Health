from django.urls import path
from .views import MedicalRecordListCreateView, MedicalRecordDetailView

urlpatterns = [
    path('medical-records/', MedicalRecordListCreateView.as_view(), name='medical-record-list-create'),
    path('medical-records/<int:pk>/', MedicalRecordDetailView.as_view(), name='medical-record-detail'),
]
