from django.db import models



class Application(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Имя'
    )
    email = models.EmailField(
        max_length=255,
        verbose_name='Почта'
    )
    number = models.CharField(
        verbose_name='Номер',
        max_length=255
    )

    summary = models.FileField(
        upload_to='summary/',
        verbose_name='Резюме'
    )
    
    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Заявление'
        verbose_name_plural = 'Заявления'
