# Generated by Django 2.2.10 on 2021-07-19 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210719_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='many_choice',
            field=models.ManyToManyField(to='api.Choice', verbose_name='Ответ выбором'),
        ),
    ]
