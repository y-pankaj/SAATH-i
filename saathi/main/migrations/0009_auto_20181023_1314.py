# Generated by Django 2.1.2 on 2018-10-23 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_personfound'),
    ]

    operations = [
        migrations.AddField(
            model_name='personfound',
            name='contact',
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AddField(
            model_name='personfound',
            name='disaster',
            field=models.CharField(default='Kerala Floods', max_length=50),
        ),
        migrations.AlterField(
            model_name='personfound',
            name='address',
            field=models.CharField(max_length=255),
        ),
    ]
