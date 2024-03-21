from django.db import models
from ckeditor.fields import RichTextField

class Faq(models.Model):
    question = models.CharField(
        max_length=255,
        verbose_name="Вопрос"
    )
    answer = RichTextField(
        verbose_name="Ответ на вопрос"
    )

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "Часто задаваемые вопросы"
        verbose_name_plural = "Часто задаваемые вопросы"
