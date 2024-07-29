from django.db import models

class Paciente(models.Model):
    Cpf = models.CharField(max_length=100)
    Nome = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Rg = models.CharField(max_length=100)
    
    def __str__(self):
        return self.Nome
    
    class Meta:
        db_table = 'Paciente'