from django.db import models


class Categorie(models.Model):
    nom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom


class Produit(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Client(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    adresse = models.CharField(max_length=255)
    telephone = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username


class Commande(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.PositiveIntegerField()
    date_commande = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return f"Commande de {self.quantite} {self.produit.nom} le {self.date_commande}"

