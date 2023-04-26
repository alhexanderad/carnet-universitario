import os
from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import Estudiante
from django.contrib import messages

def index(request):
  if request.POST:
    try:
      dni = request.POST.get('dni')
      buscar = Estudiante.objects.get(documento_1=dni)
      print(dni)

      return HttpResponseRedirect(reverse('estudiante:editAlumno', args=[dni]))
    except ObjectDoesNotExist:
      messages.success(request, "DNI NO ENCONTRADO")
      return render(request, 'index.html')

  return render(request, 'index.html', {})
def alumno(request, dni):
  alumno = get_object_or_404(Estudiante,documento_1= dni)
  print(dni)
  return render(request, 'estudiante/alumno.html', {'alumno': alumno});

def editAlumno(request, dni):
  alumno = get_object_or_404(Estudiante,documento_1= dni)
  print(dni)
  if request.method == "POST":
    if len(request.FILES) != 0:
      alumno.foto = request.FILES['foto']
    alumno.nombres = request.POST.get('nombres')
    alumno.save()
    return HttpResponseRedirect(reverse('estudiante:alumno', args=[dni]))

  return render(request, 'estudiante/editAlumno.html', {'alumno': alumno});