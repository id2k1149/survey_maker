# Generated by Django 3.0.6 on 2020-06-13 00:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('surveys_app', '0002_auto_20200612_2156'),
    ]

    operations = [
        migrations.AddField(
            model_name='monoresponse',
            name='answer',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='surveys_app.Answer'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='polyresponse',
            name='answer',
            field=models.ManyToManyField(blank=True, to='surveys_app.Answer'),
        ),
        migrations.AlterField(
            model_name='monoresponse',
            name='question',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='surveys_app.Question'),
        ),
        migrations.AlterField(
            model_name='monoresponse',
            name='survey',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='surveys_app.Survey'),
        ),
        migrations.RemoveField(
            model_name='polyresponse',
            name='question',
        ),
        migrations.AddField(
            model_name='polyresponse',
            name='question',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='surveys_app.Question'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='polyresponse',
            name='survey',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='surveys_app.Survey'),
        ),
    ]
