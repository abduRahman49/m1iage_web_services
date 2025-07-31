from django.urls import path
from .views import *


urlpatterns = [
    path('nombre-livres/', nombre_livres_view), # association (url -> view)
    path('books/<int:book_id>/', detail_livre_view), # association (url -> view)
    path('welcome/<str:username>/', WelcomeView.as_view()), # association (url -> view) appeler à chaque fois la méthode as_view() des vues basées sur des classes
    path('books/before/<int:year>/', BooksBeforeView.as_view()), # association (url -> view) appeler à chaque fois la méthode as_view() des vues basées sur des classes
    path('books/create/', BookView.as_view()), # association (url -> view) appeler à chaque fois la méthode as_view() des vues basées sur des classes
    path('home/', home), # association (url -> view) appeler à chaque fois la méthode as_view() des vues basées sur des classes
    path('user-details/', display_user_details), # association (url -> view) appeler à chaque fois la méthode as_view() des vues basées sur des classes
    path('livre/creer', CreateView.as_view(), name="creation-livre"), # association (url -> view) appeler à chaque fois la méthode as_view() des vues basées sur des classes
    path('livre/liste', display_books, name="affichage-livres"), # association (url -> view) appeler à chaque fois la méthode as_view() des vues basées sur des classes
    path('livre/update/<int:id>/', UpdateView.as_view(), name="update-livre"), # association (url -> view) appeler à chaque fois la méthode as_view() des vues basées sur des classes
]