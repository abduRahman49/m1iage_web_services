from django.urls import path
from .views import valider_commande_view, confirmer_commande_view


urlpatterns = [
    path("valider-commande/", valider_commande_view, name="valider-commande"),
    path("confirmer-commande/", confirmer_commande_view, name="confirmer-commande"),
]