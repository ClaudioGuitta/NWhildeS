# Generated by Django 2.2.1 on 2019-09-18 00:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_cliente_compra_petshop'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cliente',
        ),
        migrations.DeleteModel(
            name='Compra',
        ),
        migrations.DeleteModel(
            name='Petshop',
        ),
    ]
