from django.db import models


class Brand(models.Model):
    id = models.SmallIntegerField(verbose_name="ID", primary_key=True)
    model = models.CharField(max_length=50, verbose_name="Modelo")

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

    def __str__(self):
        return self.model
