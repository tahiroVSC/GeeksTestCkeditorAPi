from django.db import models

# Create your models here.
class Offering(models.Model):
    ICON_CHOICES = [
        ('icon1', 'Icon 1'),
        ('icon2', 'Icon 2'),
    ]
    title = models.CharField(
        max_length=255,
        verbose_name="Название"
    )
    price = models.CharField(
        max_length=255,
        verbose_name="Цена", 
        null = True, blank=True
        
    )
    photo = models.ImageField(
        upload_to='icons/', 
        choices=ICON_CHOICES, 
        verbose_name='Иконка'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"
