# Generated by Django 2.1.2 on 2018-10-19 17:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_disasters_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disasters',
            name='date_published',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
