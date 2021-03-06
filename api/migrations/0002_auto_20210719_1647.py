# Generated by Django 2.2.10 on 2021-07-19 11:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'verbose_name': 'Ответ', 'verbose_name_plural': 'Ответы'},
        ),
        migrations.AlterModelOptions(
            name='choice',
            options={'verbose_name': 'Вариант ответа', 'verbose_name_plural': 'Варианты ответа'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'Вопрос', 'verbose_name_plural': 'Вопросы'},
        ),
        migrations.AlterModelOptions(
            name='quiz',
            options={'verbose_name': 'Опрос', 'verbose_name_plural': 'Опросы'},
        ),
        migrations.AddField(
            model_name='answer',
            name='uuid',
            field=models.UUIDField(editable=False, null=True, verbose_name='Уникальный идентификатор'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='one_choice',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answers_one_choice', to='api.Choice', verbose_name='Выбранный ответ'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='api.Question', verbose_name='Вопрос'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='self_text',
            field=models.TextField(null=True, verbose_name='Ответ текстом'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='api.Question', verbose_name='Вопрос'),
        ),
        migrations.AlterField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='api.Quiz', verbose_name='Опрос'),
        ),
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.TextField(verbose_name='Текст вопроса'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='description',
            field=models.CharField(max_length=200, verbose_name='Описаниние'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='end_date',
            field=models.DateField(verbose_name='Дата окончания'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='start_date',
            field=models.DateField(auto_now_add=True, verbose_name='Дата старта'),
        ),
    ]
