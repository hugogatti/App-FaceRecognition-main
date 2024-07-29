from django.urls import path
from . import views

urlpatterns = [
    path('', views.listPrescricoes, name='listPrescricoes'),
    path('detalhes/<int:id>/', views.detalhesPrescricao, name='detalhesPrescricao'),
    path('cadastrar/', views.novaPrescricao, name='novaPrescricao'),
    path('editar/<int:id>/', views.editarPrescricao, name='editarPrescricao'),
]