# Generated by Django 2.0.13 on 2020-02-08 19:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_auto_20191202_1833'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userpessoa',
            name='user',
        ),
        migrations.AddField(
            model_name='falecomigo',
            name='data',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.DeleteModel(
            name='UserPessoa',
        ),
    ]
