from django.db import models

class Medicamento(models.Model):
    Nome = models.CharField(max_length=100)
    Codigo = models.CharField(max_length=100)
    Quantidade = models.IntegerField()
    Porta = models.IntegerField()
    DataCriacao = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.Nome
    
    class Meta:
        db_table = 'Medicamento'