# Generated by Django 3.0.6 on 2020-06-06 23:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('surveys_app', '0028_remove_pages_page_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='survey',
            name='has_pages',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='total_pages',
        ),
    ]