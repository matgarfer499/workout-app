# Generated by Django 5.0.4 on 2024-04-28 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='height',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='weight',
            field=models.FloatField(default=0),
        ),
    ]
