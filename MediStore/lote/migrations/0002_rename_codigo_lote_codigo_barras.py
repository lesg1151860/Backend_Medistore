# Generated by Django 5.1 on 2024-09-19 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lote', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lote',
            old_name='codigo',
            new_name='codigo_barras',
        ),
    ]