# Generated by Django 2.2.1 on 2019-09-27 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20190927_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sobremim',
            name='descricao_curta',
            field=models.CharField(max_length=400, null=True),
        ),
    ]