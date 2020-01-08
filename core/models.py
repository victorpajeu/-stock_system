from django.db import models


class Person(models.Model):
    name = models.CharField('Nome', max_length=200),
    age = models.IntegerField('Idade',)
    height = models.FloatField(blank=False)

