from django.views import View
from django.http import HttpResponse

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
