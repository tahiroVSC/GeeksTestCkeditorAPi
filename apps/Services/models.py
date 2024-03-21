from django.db import models


class Services(models.Model):
    title = models.CharField(
        max_length = 255,
        verbose_name = "Название"
    )
    note = models.CharField(
        max_length = 255,
        verbose_name = "Примечание"
    )
    hours_week = models.CharField(
        max_length = 255,
        verbose_name = "Кол-во часов в неделю"
    )
    price = models.CharField(
        max_length = 255,
        verbose_name = "Стоимость"
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Секция"
        verbose_name_plural = "Секции"
