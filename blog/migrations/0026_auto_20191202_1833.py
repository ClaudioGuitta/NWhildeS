# Generated by Django 2.0.13 on 2019-12-02 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_auto_20191202_1146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userpessoa',
            name='id',
        ),
        migrations.AlterField(
            model_name='userpessoa',
            name='cpf',
            field=models.CharField(blank=True, max_length=11, primary_key=True, serialize=False),
        ),
    ]