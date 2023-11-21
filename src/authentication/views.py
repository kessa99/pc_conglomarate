from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views import View
from .forms import SignUpForm
from django.urls import reverse_lazy

from django.views.generic import TemplateView, CreateView
# Create your views here.

class HomeView(TemplateView):
    template_name = 'home_index.html'

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('home')
    template_name = 'authentication/enregistrement.html'



# class SignUpView(View):
#     template_name = 'authentication/signup.html'

#     def get(self, request, *args, **kwargs):
#         form = SignUpForm()
#         return render(request, self.template_name, {'form': form})
    
#     def post(self, request, *args, **kwargs):
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('dashboard')
#         return render(request, self.template_name, {'form': form})


# class SignInView(View):
#     template_name = 'authentication/login.html'

#     def get(self, request, *args, **kwargs):
#         form = SignInForm()
#         return render(request, self.template_name, {'form': form})

#     def post(self, request, *args, **kwargs):
#         form = SignInForm(request, data=request.POST)
#         if form.is_valid():
#             user_type = form.cleaned_data.get('user_type')
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(request, username=username, password=password)
            
#             if user is not None and user_type == 'admin' and user.is_admin:
#                 login(request, user)
#                 return redirect('admin_dashboard')  # Rediriger vers le tableau de bord de l'admin
#             elif user is not None and user_type == 'employee' and not user.is_admin:
#                 login(request, user)
#                 return redirect('employee_dashboard')  # Rediriger vers le tableau de bord de l'employé
#             else:
#                 # Authentification échouée
#                 # Ajoutez le traitement approprié ici par la suite
#                 pass
        
#         return render(request, self.template_name, {'form': form})



