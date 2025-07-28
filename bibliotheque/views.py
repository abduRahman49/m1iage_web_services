from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import Book
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Create your views here.

def display_user_details(request):
    # Chaque clé représente une variable dans le template
    cours = ["Python", "Django", "Statistiques", "Probabilité"]
    context = {"nom": "Abdou SEYE", "is_graduated": False, "liste_cours": cours}
    return render(request, "bibliotheque/users_detail.html", context)

def home(request):
    nom = "Abdou SEYE"
    context = {"nom": nom, "is_graduated": True}
    return render(request, "bibliotheque/index.html", context)

@csrf_exempt
def hello_view(request, username=None):
    message = f"Bonjour, {username} ! Bienvenue sur la bibliothèque."
    return HttpResponse(message)


def nombre_livres_view(request):
    nombre_livres = Book.objects.count()
    return HttpResponse(f"Il y a actuellement {nombre_livres} livres enregistrés.")


def detail_livre_view(request, book_id):
    try:
        livre = Book.objects.get(id=book_id)
        message = f"""
            Titre: {livre.title} \n
            Auteur: {livre.author} \n
            Date publication : {livre.published_year}
        """
        return HttpResponse(message)
    except Book.DoesNotExist:
        return HttpResponse("Le livre demandé n'existe pas")


class WelcomeView(View):

    def get(self, request, username):
        message = f"Bonjour, {username} ! Bienvenue sur la bibliothèque."
        return HttpResponse(message)


class BooksBeforeView(View):

    def get(self, request, year):
        books_before = Book.objects.filter(published_year__lt=year)
        if books_before.exists():
            livres_formattes = ", ".join(f"""
                {livre.author}, {livre.published_year}, {livre.title}
            """ for livre in books_before)

            message = f"""
                Les livres publiés avant {year} : {livres_formattes}
            """
            return HttpResponse(message)
        return HttpResponse("Aucun livre ne correspond à ce critère de recherche")


@method_decorator(csrf_exempt, name="dispatch")
class BookView(View):

    def get(self, request):
        return HttpResponse("Utilisez POST pour ajouter un livre.")
    
    def post(self, request):
        title = request.POST.get("title")
        author = request.POST.get("author")
        published_year = request.POST.get("published_year")
        book = Book.objects.create(title=title, author=author, published_year=published_year)
        return HttpResponse(f"Vous avez créé le livre avec l'id {book.id} et intitulé {book.title}")


class CreateView(View):

    def get(self, request):
        return render(request, "bibliotheque/creation_livre.html")
    
    def post(self, request):
        titre = request.POST.get("titre")
        auteur = request.POST.get("auteur")
        date_publication = request.POST.get("date_publication")
        livre = Book.objects.create(title=titre, author=auteur, published_year=date_publication)
        return HttpResponse(f"Vous avez créé le livre {livre.id} intitulé {livre.title}")
    

def display_books(request):
    books = Book.objects.all()
    context = {"livres": books}
    return render(request, "bibliotheque/liste_livres.html", context)
