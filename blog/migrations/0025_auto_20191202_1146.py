# Generated by Django 2.0.13 on 2019-12-02 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_userpessoa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userpessoa',
            name='sexo',
        ),
        migrations.AddField(
            model_name='userpessoa',
            name='cpf',
            field=models.CharField(blank=True, max_length=11),
        ),
    ]
