from django.urls import path
from . import views

urlpatterns = [
    # Professors
    path('guardar_sesion/', views.guardar_sesion, name='guardar_sesion'),
    path('recuperar_sesion/', views.recuperar_sesion, name='recuperar_sesion'),
]