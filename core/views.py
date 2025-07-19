from django.views import View
from django.http import HttpResponse
from .models import Tache


# Vue basée sur une fonction (FBV: Function-based view)
def hello_view(request, nom=None):
    # Visualisation de certaines informations liées à la requête
    print("La méthode de la requête", request.method)
    print("Les en-têtes de la requête", request.headers)
    print("L'url de la requête", request.path)
    print("Les informations de l'url de la requête", request.path_info)

    # Envoi de la réponse
    message = f"Hello {nom} from FBV" if nom else "Hello world from FBV"
    return HttpResponse(message)


# Vue basée sur une classe (CBV: Class-based view)
class HiView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse("Hi world from CBV")

    def post(self, request, *args, **kwargs):
        #
        return HttpResponse("Vous avez appelé la méthode POST!")
    

def detail_tache_view(request, id):
    try:
        print("La valeur de q", request.GET.get("q")) # Récupération des paramètres d'url
        tache = Tache.objects.get(id=id)
        infos_tache = f"""
            La tache est intitulée {tache.libelle} \n
            Elle a été créée le {tache.date_creation.isoformat()} \n
            Voici sa description: {tache.description}
        """
        return HttpResponse(infos_tache)
    except Tache.DoesNotExist:
        return HttpResponse("La tâche n'existe pas")
