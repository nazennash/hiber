# Generated by Django 5.0.3 on 2024-04-25 22:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Leads',
            new_name='Lead',
        ),
    ]