# Generated by Django 4.1.3 on 2023-01-05 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appPerfiles', '0002_informacionperfil'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='informacionperfil',
            name='biografía',
        ),
        migrations.AddField(
            model_name='informacionperfil',
            name='biografia',
            field=models.TextField(default='Hola'),
        ),
    ]
