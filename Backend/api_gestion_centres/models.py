from django.db import models
from django.contrib.auth.models import User

class Centre(models.Model):
    nom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=200)
    administrateur = models.ForeignKey(User, on_delete=models.CASCADE)

    # Relation pour les abonnements
    abonnements = models.ManyToManyField('Abonnement', related_name='centres')

    # Relation pour les messages reçus
    messages = models.ManyToManyField('Message', related_name='centres')

class Abonnement(models.Model):
    centre = models.ForeignKey(Centre, on_delete=models.CASCADE)
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    date_abonnement = models.DateTimeField(auto_now_add=True)
    valide = models.BooleanField(default=False)

class Message(models.Model):
    centre = models.ForeignKey(Centre, on_delete=models.CASCADE)
    expediteur = models.ForeignKey(User, on_delete=models.CASCADE)
    destinataire = models.CharField(max_length=100)
    contenu = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)

    @property
    def nom(self):
        return self.contenu
