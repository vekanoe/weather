from django.db import models


class City(models.Model):
    """ Город """

    title = models.CharField('Наименование', max_length=250, unique=True)
    lat = models.DecimalField('Широта', max_digits=5, decimal_places=2)
    lon = models.DecimalField('Долгота', max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return self.title
