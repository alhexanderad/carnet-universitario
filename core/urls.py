
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from estudiante.views import index

urlpatterns = [
  path('admin/', admin.site.urls),
  path('',index, name='index'),
  path('alumno/', include('estudiante.urls', namespace='estudiante'))
]
if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
