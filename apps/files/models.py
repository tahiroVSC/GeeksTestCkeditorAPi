from django.db import models

# Create your models here.


class File(models.Model):
    name = models.CharField(max_length=40,verbose_name="Название_файла")
    file = models.FileField(null=True,blank= True,upload_to='files/', verbose_name= 'Файл')




    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Файл',
        verbose_name_plural = 'Файлы'