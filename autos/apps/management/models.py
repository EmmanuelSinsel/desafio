from django.db import models

from apps.car.models import Car


class Management(models.Model):
    #id = models.SmallIntegerField(verbose_name='ID', primary_key=True)
    km = models.IntegerField(verbose_name='Kilometrage')
    desc = models.CharField(verbose_name="Descripcion", max_length=150)
    cost = models.FloatField(verbose_name="Costo")
    date = models.DateField(verbose_name="Fecha de mantenimiento")
    auto = models.ForeignKey(Car, on_delete=models.CASCADE,
                             null=True, verbose_name='Auto')

    class Meta:
        verbose_name = 'Mantenimiento'
        verbose_name_plural = 'Mantenimientos'

    def __str__(self):
        return '%s' % (self.desc)
