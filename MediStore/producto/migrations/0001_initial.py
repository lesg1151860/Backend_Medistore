# Generated by Django 5.1 on 2024-09-02 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_producto', models.CharField(max_length=255)),
                ('codigo_invima', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
    ]