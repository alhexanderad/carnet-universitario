# Generated by Django 4.0 on 2023-04-27 00:20

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estudiante', '0007_alter_estudiante_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='foto',
            field=cloudinary.models.CloudinaryField(default='media/default-img.jpg', max_length=255, verbose_name='image'),
        ),
    ]