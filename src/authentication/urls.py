from django.urls import path
from .views import *

urlpatterns = [
    path('admin_signup', admin_signup, name='admin_signup'),
    path('empl', empl, name='empl'),
    path('admin', admin, name='admin'),
]
