from django.db import models
from ckeditor.fields import RichTextField



class Abonement(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    description = RichTextField(verbose_name='Описание')
    time = models.CharField(max_length=150, verbose_name='Время посещения')
    price = models.CharField(
        max_length=20, verbose_name='Стоимость')
    special = models.BooleanField(verbose_name='Специальное предложение?')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Абонемент',
        verbose_name_plural = 'Абонементы'