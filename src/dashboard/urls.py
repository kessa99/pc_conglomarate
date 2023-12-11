from django.urls import path
from .views import *

urlpatterns = [
    # URL POUR LE CAS EMPLOYE
    path('dash_empl/', dash_empl, name='dash_empl'),
    path('profil_employe/', profil_employe, name='profil_employe'),
    path('profil_admin/', profil_admin, name='profil_admin'),
    path('modifier_id/', modifier_id, name='modifier_id'),
    path('modifier_profile/', modifier_profile, name='modifier_profile'),

    # URL POUR LE CAS ADMIN
    path('dash_admin/', dash_admin, name='dash_admin'),
    path('profil_admin/', profil_admin, name='profil_admin'),
    path('create_compte/', create_compte, name='create_compte'),
    path('zone_work/', zone_work, name='zone_work'),
]