# Generated by Django 5.0 on 2024-03-19 07:09

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Type_of_trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название вида тренировки')),
                ('name_ru', models.CharField(max_length=100, null=True, verbose_name='Название вида тренировки')),
                ('name_ky', models.CharField(max_length=100, null=True, verbose_name='Название вида тренировки')),
            ],
            options={
                'verbose_name': ' Вид тренера',
                'verbose_name_plural': 'Виды  тренеров',
            },
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Фамилия Имя')),
                ('name_ru', models.CharField(max_length=250, null=True, verbose_name='Фамилия Имя')),
                ('name_ky', models.CharField(max_length=250, null=True, verbose_name='Фамилия Имя')),
                ('photo', models.ImageField(upload_to='trainer/', verbose_name='Изображение')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Описание')),
                ('description_ru', ckeditor.fields.RichTextField(null=True, verbose_name='Описание')),
                ('description_ky', ckeditor.fields.RichTextField(null=True, verbose_name='Описание')),
                ('type_of_trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trainer.type_of_trainer', verbose_name='Вид тренера')),
            ],
            options={
                'verbose_name': 'Тренер',
                'verbose_name_plural': 'Тренера',
            },
        ),
    ]