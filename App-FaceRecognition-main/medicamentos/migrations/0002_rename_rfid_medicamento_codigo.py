# Generated by Django 5.0.1 on 2024-05-18 02:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicamentos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medicamento',
            old_name='RFID',
            new_name='Codigo',
        ),
    ]
