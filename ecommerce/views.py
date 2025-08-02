from django.shortcuts import render
from django.contrib.auth.decorators import permission_required


@permission_required("ecommerce.valider_commande")
def valider_commande_view(request):
    return render(request, "ecommerce/confirmer_commande.html")


@permission_required("ecommerce.confirmer_commande")
def confirmer_commande_view(request):
    return render(request, "ecommerce/valider_commande.html")
