from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class TrainZone(models.Model):
    photo = models.ImageField(null=True, blank=True,verbose_name='Фото')
    title = models.CharField(max_length=100, verbose_name='Название')
    description = RichTextField(verbose_name='Описание')


    def __str__(self):
        return self.title



    class Meta:
        verbose_name = 'Зона',
        verbose_name_plural = 'Зоны'