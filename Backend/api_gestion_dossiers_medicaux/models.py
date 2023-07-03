from django.db import models
from api_gestion_patients.models import Patient

class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    consultation_date = models.DateField()
    diagnosis = models.CharField(max_length=200)
    treatment = models.CharField(max_length=200)
    prescription = models.CharField(max_length=200)
    exam_results = models.CharField(max_length=200)

    def __str__(self):
        return f"Medical Record for {self.patient}"
