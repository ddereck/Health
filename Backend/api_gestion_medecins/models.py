from django.db import models

class Doctor(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    specialite = models.ForeignKey('Specialty', on_delete=models.CASCADE)
    adresse = models.CharField(max_length=100)
    # Autres champs pour les informations sur le médecin

class Specialty(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    # Autres champs pour les informations sur les spécialités médicales

class Availability(models.Model):
    medecin = models.ForeignKey('Doctor', on_delete=models.CASCADE)
    date = models.DateField()
    heure_debut = models.TimeField()
    heure_fin = models.TimeField()
    # Autres champs pour les informations sur les disponibilités des médecins
