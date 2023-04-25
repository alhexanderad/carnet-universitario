# Generated by Django 4.0 on 2023-04-25 23:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primer_apellido', models.CharField(max_length=120)),
                ('segundo_apellido', models.CharField(max_length=120)),
                ('nombres', models.CharField(max_length=120)),
                ('tipo_documento', models.CharField(choices=[('1', 'Documento Nacional de Identidad'), ('2', 'Pasaporte'), ('3', 'Carné de Extranjería'), ('4', 'Cédula de identidad'), ('5', 'Documento Extranjero - Otros'), ('6', 'Permiso Temporal de Permanencia'), ('7', 'Carné de Identidad')], default='Carné de Identidad', max_length=100)),
                ('documento_1', models.CharField(max_length=8, unique=True, validators=[django.core.validators.RegexValidator(message='Debe de ingresar los 8 digitos de DNI', regex='^\\+?1?\\d{8}')])),
                ('pasporte', models.CharField(max_length=9, unique=True)),
                ('codigo_matricula', models.CharField(max_length=15, unique=True)),
                ('email_est', models.EmailField(max_length=254)),
                ('telefono_est', models.CharField(max_length=9, validators=[django.core.validators.RegexValidator(message='Debe de ingresar el numero de 9 digitos', regex='^\\+?1?\\d{9,15}')])),
                ('foto', models.ImageField(upload_to='images/')),
                ('fecha_ingreso', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizar', models.DateTimeField(auto_now=True)),
            ],
            options={
                'get_latest_by': 'fecha_ingreso',
            },
        ),
    ]