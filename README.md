# Centro-Educativo

# views.py
from django.shortcuts import render, get_object_or_404
from seccion.models import Secciones
from estudiante.models import Estudiante
from asignatura.models import Asignatura


# views.py
from django.shortcuts import render, get_object_or_404
from seccion.models import Secciones
from estudiante.models import Estudiante
from asignatura.models import Asignatura

def listar_estudiantes2(request, seccion_id):
    # Obtener la sección y los estudiantes asociados
    seccion = get_object_or_404(Secciones, id=seccion_id)
    estudiantes = Estudiante.objects.filter(seccion=seccion)
    asignaturas = Asignatura.objects.filter(grado=seccion.grado)  # Las asignaturas del grado de la sección

    return render(request, 'listar_estudiantes_calificacion.html', {
        'seccion': seccion,
        'estudiantes': estudiantes,
        'asignaturas': asignaturas,
    })
# views.py


def listar_estudiantes_calificacion(request, seccion_id):
    seccion = get_object_or_404(Secciones, id=seccion_id)
    estudiantes = Estudiante.objects.filter(seccion=seccion)  # Estudiantes de esta sección
    asignaturas = Asignatura.objects.filter(grado=seccion.grado)  # Las asignaturas del grado de la sección
    
    return render(request, 'listar_estudiantes_calificacion.html', {
        'seccion': seccion,
        'estudiantes': estudiantes,
        'asignaturas': asignaturas,
    })


# views.py
from django.shortcuts import render, get_object_or_404
from .forms import CalificacionForm
from seccion.models import Secciones
from estudiante.models import Estudiante
from asignatura.models import Asignatura

def agregar_calificacion(request, seccion_id, estudiante_id):
    seccion = get_object_or_404(Secciones, id=seccion_id)
    estudiante = get_object_or_404(Estudiante, id=estudiante_id)
    asignaturas = Asignatura.objects.filter(grado=seccion.grado)  # Asignaturas del grado de la sección

    if request.method == 'POST':
        for asignatura in asignaturas:
            # Obtener la calificación para cada asignatura
            nota = request.POST.get(f'nota_{asignatura.id}')
            if nota:
                # Crear o actualizar la calificación
                calificacion, created = Calificacion.objects.update_or_create(
                    estudiante=estudiante, asignatura=asignatura,
                    defaults={'nota': nota}
                )
        return redirect('listar_estudiantes_calificacion', seccion_id=seccion.id)  # Redirigir a la lista de estudiantes
    
    return render(request, 'agregar_calificacion.html', {
        'seccion': seccion,
        'estudiante': estudiante,
        'asignaturas': asignaturas,
    })



