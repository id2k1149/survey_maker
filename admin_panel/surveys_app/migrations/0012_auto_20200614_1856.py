# Generated by Django 3.0.6 on 2020-06-14 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('surveys_app', '0011_auto_20200614_1855'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='response',
            options={'verbose_name': 'Полученный ответ', 'verbose_name_plural': 'Полученные ответы'},
        ),
    ]
