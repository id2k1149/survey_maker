# Generated by Django 3.0.6 on 2020-05-31 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('surveys_app', '0019_auto_20200531_1814'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='namedpages',
            name='survey',
        ),
        migrations.AddField(
            model_name='survey',
            name='bye_text',
            field=models.TextField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='survey',
            name='bye_title',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='survey',
            name='hello_text',
            field=models.TextField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='survey',
            name='hello_title',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='survey',
            name='info_text',
            field=models.TextField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='survey',
            name='info_title',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='survey',
            name='status',
            field=models.ForeignKey(blank=True, default='1', null=True, on_delete=django.db.models.deletion.CASCADE, to='surveys_app.StatusType'),
        ),
        migrations.DeleteModel(
            name='InfoPage',
        ),
        migrations.DeleteModel(
            name='NamedPages',
        ),
    ]