from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
# import le décorateur à appliquer
from django.contrib.auth.decorators import login_required
# import la façon de l'appliquer à une vue basée sur une classe
from django.utils.decorators import method_decorator


class InscritionView(View):
    def get(self, request):
        roles = [role.name for role in Group.objects.all()]
        context = {"roles": roles}
        return render(request, 'authentification/inscription.html', context)

    def post(self, request):
        # Handle form submission logic here
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # récupération du role
        role = request.POST.get("role")
        group = Group.objects.filter(name=role).first()
        user = User.objects.create_user(username=username, email=email, password=password)
        user.groups.add(group)
        return HttpResponse(f"L'utilisateur {user.username} a été créé avec succès!")


def index_view(request):
    return render(request, "authentification/index.html")

class LoginView(View):

    def get(self, request):
        return render(request, 'authentification/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        print("Username", username)
        print("Password", password)
        user = authenticate(username=username, password=password)
        print("User", user)
        if user is not None:
            login(request, user)
            return redirect("home")
        return HttpResponse("Login successful!")  # Placeholder for actual login logic
    

def logout_view(request):
    logout(request)
    return redirect("login-view")

# Tant qu'on est pas déjà connecté on ne pourra accéder à la vue
@method_decorator(login_required, name="dispatch")
class UpdatePasswordView(View):

    def get(self, request):
        return render(request, "authentification/password_reset.html")

    def post(self, request):
        password = request.POST.get("password")
        # récupération de l'utilisateur depuis l'objet request
        # autre option User.objects.get(username=username)
        user = request.user
        # modification du mot de passe
        user.set_password(password) # set_password déconnecte automatiquement la session
        # sauvegarde de l'utilisateur
        user.save()
        # redirige l'utilisateur à la page de connexion
        return redirect("login-view")