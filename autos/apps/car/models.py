from django.db import models

from apps.model.models import carModel
from apps.user.models import User


class Car(models.Model):
    plate = models.CharField(max_length=10, verbose_name="Placa")
    km = models.IntegerField(verbose_name="Kilometrage")
    car = models.ForeignKey(carModel, on_delete=models.CASCADE, related_name="model", null=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,
                               related_name='Name',)
    class Meta:
        verbose_name = 'Auto'
        verbose_name_plural = 'Autos'

    def __str__(self):
        return '%s' % (self.plate)
