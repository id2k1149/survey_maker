# Generated by Django 3.0.6 on 2020-05-13 01:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('surveys_app', '0004_survey'),
        ('reports_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='survey',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='surveys_app.Survey'),
            preserve_default=False,
        ),
    ]
