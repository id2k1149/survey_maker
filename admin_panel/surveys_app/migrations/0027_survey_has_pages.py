# Generated by Django 3.0.6 on 2020-06-02 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys_app', '0026_survey_total_pages'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='has_pages',
            field=models.BooleanField(default=False),
        ),
    ]