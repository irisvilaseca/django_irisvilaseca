
from django.urls import path
from . import views

urlpatterns = [
    # Professors
    path('teachers/', views.llistat_professors, name='llistat_professors'),
    path('teachers/<int:id>/', views.detall_professor, name='detall_professor'),
    
    # Alumnes
    path('students/', views.llistat_alumnes, name='llistat_alumnes'),
    path('students/<int:id>/', views.detall_alumne, name='detall_alumne'),
]
