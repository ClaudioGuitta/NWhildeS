# Generated by Django 2.1.2 on 2019-10-01 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_sobremim_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='sobremim',
            name='sobre',
            field=models.TextField(blank=True, max_length=50, null=True),
        ),
    ]
