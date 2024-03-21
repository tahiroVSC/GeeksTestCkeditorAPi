from django.db import models
from ckeditor.fields import RichTextField


class AboutUs(models.Model):
    text = RichTextField(verbose_name='Текст')
    add_text = RichTextField(verbose_name='Доп. Текст')
    
    def __str__(self):
        return 'О нас'

    class Meta:
        verbose_name = 'О нас',
        verbose_name_plural = 'О нас'
