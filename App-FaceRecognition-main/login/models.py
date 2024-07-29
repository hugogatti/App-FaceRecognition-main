from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    login = models.ForeignKey(User, models.PROTECT, null=False, blank=False, related_name='UserLogin',
                              verbose_name='UserLogin')

    Cpf = models.CharField(max_length=100)
    Nome = models.CharField(max_length=100)

    Crm = models.CharField(max_length=100)
    Rg = models.CharField(max_length=100)
    ReconhecimentoFacial = models.ImageField(upload_to='ReconhecimentoFacial', null=True, blank=True)
    TipoUsuario = models.CharField(max_length=20)

    def __str__(self):
        return self.Cpf

    class Meta:
        db_table = 'UserProfile'
def get_username(self):
    return self.username

User.add_to_class("__str__", get_username)