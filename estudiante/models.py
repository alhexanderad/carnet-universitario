import cloudinary.uploader
from django.db import models
from django.core.validators import RegexValidator
from cloudinary.models import CloudinaryField

class Estudiante(models.Model):
  DOCUMENTO =(
    ('1','Documento Nacional de Identidad'),
    ('2','Pasaporte'),
    ('3','Carné de Extranjería'),
    ('4','Cédula de identidad'),
    ('5','Documento Extranjero - Otros'),
    ('6','Permiso Temporal de Permanencia'),
    ('7','Carné de Identidad'),
    )

  primer_apellido = models.CharField(max_length=120)
  segundo_apellido = models.CharField(max_length=120)
  nombres = models.CharField(max_length=120)
  tipo_documento = models.CharField(max_length=100, choices=DOCUMENTO, default='Carné de Identidad')
  dni_regex = RegexValidator(regex=r'^\+?1?\d{8}', message = ("Debe de ingresar los 8 digitos de DNI"))
  documento_1 = models.CharField(validators=[dni_regex], max_length=8, unique=True)
  codigo_matricula = models.CharField(max_length=15, unique=True)
  email_est = models.EmailField()
  telefono_regex = RegexValidator(regex=r'^\+?1?\d{9,15}', message = ("Debe de ingresar el numero de 9 digitos"))
  telefono_est = models.CharField(validators=[telefono_regex], max_length=9, blank=False)
  foto = CloudinaryField('image', default='media/default-img.jpg')
  fecha_ingreso = models.DateTimeField(auto_now_add=True)
  fecha_actualizar = models.DateTimeField(auto_now=True)

  def save(self, *args, **kwargs):
    cloudinary.uploader.upload(self.foto, folder="carnet-universitario", public_id='1_{}'.format(self.documento_1))
    super().save(*args, **kwargs)
  class Meta:
    get_latest_by = 'fecha_ingreso'

  def __str__(self):
    return "{} , {} ".format(self.primer_apellido[:25], self.segundo_apellido[:25], self.nombres[:25])


