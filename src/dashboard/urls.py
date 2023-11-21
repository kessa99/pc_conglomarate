from django.urls import path
from . import views

urlpatterns = [
    path('index_page/', views.index_page, name='index_page'),
]