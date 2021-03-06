# Generated by Django 3.2.4 on 2021-06-20 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amir_music', '0005_auto_20191218_1238'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='grupo',
            options={'ordering': ['-fecha_fundacion', 'nombre']},
        ),
        migrations.AlterModelOptions(
            name='musico',
            options={'ordering': ['grupo', 'nombre']},
        ),
        migrations.AddField(
            model_name='album',
            name='cover',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
