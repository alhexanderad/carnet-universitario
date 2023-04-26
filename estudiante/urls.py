from django.urls import path
from .views import alumno, editAlumno

app_name = "estudiante"
urlpatterns = [
  path('<int:dni>', alumno, name='alumno'),
  path('editar/<int:dni>', editAlumno, name='editAlumno'),
]
