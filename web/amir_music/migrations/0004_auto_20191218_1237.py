# Generated by Django 2.2.8 on 2019-12-18 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amir_music', '0003_auto_20191114_1026'),
    ]

    operations = [
        migrations.AddField(
            model_name='musico',
            name='lat',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='musico',
            name='lon',
            field=models.FloatField(null=True),
        ),
    ]
