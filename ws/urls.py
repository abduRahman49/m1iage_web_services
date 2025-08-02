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
from django.urls import path, include
from core.views import hello_view, HiView, detail_tache_view, liste_taches_view
from authentification.views import InscritionView, LoginView, index_view, logout_view, UpdatePasswordView


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('hello/<str:nom>/', hello_view), # association (url -> view)
    # path('hi/', HiView.as_view()), # association (url -> view)
    # path('tache/<int:id>/', detail_tache_view), # association (url -> view)
    path('liste-taches/', liste_taches_view), # association (url -> view)
    path('hello/<str:username>/', hello_view), # association (url -> view)
    path('bibliotheque/', include("bibliotheque.urls")), # association (url -> view)
    path('authentification/inscription/', InscritionView.as_view(), name="inscription"),
    path('authentification/connexion/', LoginView.as_view(), name="login-view"),
    path('authentification/logout/', logout_view, name="logout-view"),
    path('authentification/update-password/', UpdatePasswordView.as_view(), name="update-view"),
    path('home/', index_view, name="home"),
    path('ecommerce/', include("ecommerce.urls"))
]
