# Generated by Django 3.0.6 on 2020-06-12 01:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('surveys_app', '0004_auto_20200612_0128'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OfferedAnswer',
            new_name='Answer',
        ),
    ]
