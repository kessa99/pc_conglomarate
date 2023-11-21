from django.urls import path
from .views import HomeView, SignUpView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name = 'authentication/connexion.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # path('signup/', views.enregistrement, name='signup'),
    # path('login/', views.connexion, name='login'),
    # path('', views.home, name='home'),
    # path('logout/', auth_views.LogoutView.as_view()),
]