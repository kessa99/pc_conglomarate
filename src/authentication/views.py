from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt



def signup(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            print('valid')
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Compte créé pour {username}")
            return redirect('login')
        else:
            # Ajouter les messages d'erreur à afficher dans le template
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
    context = {'form': form}
    return render(request, 'registration/signup.html', context)


@csrf_exempt
def user_login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'registration/login.html', {'form': form})

    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password1')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f"Connexion réussie en tant que {username}")
                return redirect('home')
            else:
                messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
        else:
            # Ajouter les messages d'erreur à afficher dans le template
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
            
            form = LoginForm()
    else:
        form = LoginForm()

    context = {'form': form}
    return render(request, 'registration/login.html', context)

def user_logout(request):
    logout(request)
    messages.info(request, "Vous avez été déconnecté.")
    return redirect('login')