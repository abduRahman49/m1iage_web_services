from django.db import models
from django.conf import settings

# Create your models here.

class ListeTache(models.Model):
    libelle = models.CharField(max_length=255)


class Categorie(models.Model):
    libelle = models.CharField(max_length=255)


class Tache(models.Model):
    libelle = models.CharField(max_length=100)
    description = models.CharField(max_length=255, null=True)
    est_terminee = models.BooleanField(default=False)
    date_creation = models.DateTimeField(auto_now_add=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, null=True) # plusieurs à un
    listes_taches = models.ManyToManyField(ListeTache) # plusieurs à plusieurs


class Profil(models.Model):
    ADMIN = "Admin"
    SUPERVISEUR = "Superviseur"
    STANDARD = "Standard"

    PROFIL = (
        (ADMIN, 'admin'),
        (SUPERVISEUR, 'superviseur'),
        (STANDARD, 'standard')
    )
    libelle = models.CharField(choices=PROFIL, default=STANDARD)
    utilisateur = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    ) # un à un
