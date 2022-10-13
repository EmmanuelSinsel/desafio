from django.db import models

from apps.brand.models import Brand

class carModel(models.Model):
    id = models.SmallIntegerField(verbose_name="ID", primary_key=True)
    name = models.CharField(max_length=100, verbose_name='Modelo')
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL,
                                 null=True, verbose_name='Marca')
    class Meta:
        verbose_name = 'Modelo'
        verbose_name_plural = 'Modelos'

    def __str__(self):
        return self.name
