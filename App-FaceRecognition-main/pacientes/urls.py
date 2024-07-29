from django.urls import path
from . import views

urlpatterns = [
    path('', views.listPacientes, name='listPacientes'),
    path('detalhesPaciente/<int:id>', views.detalhesPaciente, name='detalhesPaciente'),
    path('novoPaciente/', views.novoPaciente, name='novoPaciente'),
    path('editarPaciente/<int:id>', views.editarPaciente, name='editarPaciente'),    
]