# Generated by Django 2.1.2 on 2019-10-01 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_sobremim_descricao_curta'),
    ]

    operations = [
        migrations.CreateModel(
            name='MeuBlog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fotos', models.ImageField(upload_to='media/%Y/%m/%D')),
            ],
        ),
    ]