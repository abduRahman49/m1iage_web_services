"""
URL configuration for ws project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import hello_view, HiView, detail_tache_view, liste_taches_view
from bibliotheque.views import hello_view, nombre_livres_view, detail_livre_view, WelcomeView, BooksBeforeView, BookView, home, display_user_details

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('hello/<str:nom>/', hello_view), # association (url -> view)
    # path('hi/', HiView.as_view()), # association (url -> view)
    # path('tache/<int:id>/', detail_tache_view), # association (url -> view)
    path('liste-taches/', liste_taches_view), # association (url -> view)
    path('hello/<str:username>/', hello_view), # association (url -> view)
    path('nombre-livres/', nombre_livres_view), # association (url -> view)
    path('books/<int:book_id>/', detail_livre_view), # association (url -> view)
    path('welcome/<str:username>/', WelcomeView.as_view()), # association (url -> view) appeler à chaque fois la méthode as_view() des vues basées sur des classes
    path('books/before/<int:year>/', BooksBeforeView.as_view()), # association (url -> view) appeler à chaque fois la méthode as_view() des vues basées sur des classes
    path('books/create/', BookView.as_view()), # association (url -> view) appeler à chaque fois la méthode as_view() des vues basées sur des classes
    path('home/', home), # association (url -> view) appeler à chaque fois la méthode as_view() des vues basées sur des classes
    path('user-details/', display_user_details), # association (url -> view) appeler à chaque fois la méthode as_view() des vues basées sur des classes
]
