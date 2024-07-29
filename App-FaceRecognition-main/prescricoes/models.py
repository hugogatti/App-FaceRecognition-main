from django.db import models
from pacientes.models import Paciente
from medicamentos.models import Medicamento
from login.models import UserProfile

class Prescricao(models.Model):
    Medico = models.ForeignKey(UserProfile, null=True, on_delete=models.SET_NULL)
    Paciente = models.ForeignKey(Paciente, null=True, on_delete=models.SET_NULL)
    Medicamentos = models.ManyToManyField(Medicamento)
    Data = models.DateTimeField(auto_now_add=True)
    Ativo = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.Id)
    
    class Meta:
        db_table = 'Prescricao'