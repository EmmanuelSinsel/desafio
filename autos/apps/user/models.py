from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    #username =  models.CharField(max_length=50, verbose_name="Nombre de usuario")
    #name = models.CharField(max_length=50, verbose_name="Nombre")
    #lastname = models.CharField
    class Type(models.IntegerChoices):
        ADMIN = (0, 'Admin')
        CLIENTE = (1, 'Cliente')

    type = models.IntegerField(verbose_name='Tipo', choices=Type.choices,
                               default=Type.ADMIN)

    class Meta:
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)
