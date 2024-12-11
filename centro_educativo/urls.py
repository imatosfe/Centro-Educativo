"""
URL configuration for centro_educativo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.urls import include

from usuarios_app.views import Login, logout_usuario

from django.urls import path, include

from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pagina_principal.urls')),

path('estudiantes/', include('estudiante.urls')), 
    path('aulas/', include('aula.urls')),
    path('profesores/', include('profesor.urls')),   # Asegúrate que el nombre sea correcto
    path('usuarios/', include('usuarios_app.urls')), # Asegúrate que el nombre sea
     path('grados/', include('grado.urls')), # Asegúrate que el nombre sea
      path('secciones/', include('seccion.urls')), # Asegúrate que el nombre sea
   
     path('asignatura/', include('asignatura.urls')), # Asegúrate que el nombre sea
          path('calificaciones/', include('calificaion.urls')), # Asegúrate que el nombre sea
     
   




    path('accounts/login',Login.as_view(), name = 'login'),
    path('logout/',logout_usuario ,name = 'logout'),

]
# Esto es opcional, pero útil si tienes archivos estáticos o multimedia
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
