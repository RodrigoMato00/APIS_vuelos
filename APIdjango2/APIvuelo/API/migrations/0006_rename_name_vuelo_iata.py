# Generated by Django 4.1.1 on 2022-10-20 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0005_rename_iata_vuelo_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vuelo',
            old_name='name',
            new_name='IATA',
        ),
    ]