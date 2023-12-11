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


def empl(request):
    return render(request, 'empl_home.html', {})

def admin(request):
    return render(request, 'admin_home.html', {})