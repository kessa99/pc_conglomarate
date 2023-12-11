from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def admin_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Connexion automatique de l'administrateur après l'inscription
            login(request, user)
            return redirect('accueil')  # Redirigez l'utilisateur où vous voulez
    else:
        form = UserCreationForm()
    return render(request, 'admin_signup.html', {'form': form})

def dash_empl(request):
    return render(request, 'dashboard/dash_empl.html', {})

def dash_admin(request):
    return render(request, 'dashboard/dash_admin.html', {})

def profil_employe(request):
    return render(request, 'dashboard/profile_empl.html', {})

def profil_admin(request):
    return render(request, 'dashboard/profile_admin.html', {})

def modifier_id(request):
    return render(request, 'dashboard/modifier_id.html', {})

def modifier_profile(request):
    return render(request, 'dashboard/modifier_profil.html', {})

# ADMIN

def profil_admin(request):
    return render(request, 'dashboard/profile_admin.html', {})

def create_compte(request):
    return render(request, 'dashboard/create_compte.html', {})

def zone_work(request):
    return render(request, 'dashboard/zone_work.html', {})