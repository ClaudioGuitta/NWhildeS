# Generated by Django 2.2.1 on 2019-09-27 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_post_descricao_curta'),
    ]

    operations = [
        migrations.AddField(
            model_name='sobremim',
            name='descricao_curta',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='descricao_curta',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
