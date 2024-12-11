# secciones/views.py
from django.shortcuts import render, redirect, get_object_or_404
from seccion.models import Secciones
from .forms import SeccionForm
from django.contrib import messages

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from grado.models import Grado
import json


from django.shortcuts import render, get_object_or_404
from estudiante.models import Estudiante
from seccion.models import Secciones

def lista_secciones(request):
    secciones = Secciones.objects.all()  # Obtén todas las secciones
    return render(request, 'lista_secciones.html', {
        'secciones': secciones,
    })


def crear_seccion(request):
    if request.method == 'POST':
        form = SeccionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sección creada con éxito.')
            return redirect('lista_secciones')
        else:
            messages.error(request, 'Error al crear la sección.')
    else:
        # Si el método es GET, muestra un formulario vacío
        form = SeccionForm()
    
    # Renderiza la plantilla con el formulario (vacío o con errores)
    return render(request, 'crear_seccion.html', {'form': form})







def editar_seccion(request, seccion_id):
    seccion = get_object_or_404(Secciones, id=seccion_id)
    if request.method == 'POST':
        seccion_form = SeccionForm(request.POST, instance=seccion)
        if seccion_form.is_valid():
            seccion_form.save()
            messages.success(request, ' sección actualizado exitosamente.')
            return redirect('lista_secciones')
        else:
            messages.error(request, 'Error al actualizar la sección.')
    else:
      
        seccion_form = SeccionForm(instance=seccion)
    return render(request, 'crear_seccion.html', {'form': seccion_form, 'editar': True})






@csrf_exempt  
def eliminar_seccion(request, seccion_id):
    if request.method == 'POST':
        # Intenta obtener el estudiante por ID
        seccione = get_object_or_404(Secciones, id=seccion_id)
        
        try:
            seccione.delete()  # Intenta eliminar el estudiante
            messages.success(request, 'Sección eliminada exitosamente.')
            return JsonResponse({'success': True})
        
        except Exception as e:
            messages.success(request, 'Error al Eliminar.')
            return JsonResponse({'success': False, 'error': str(e)})
    else:
        messages.error(request, 'Error al eliminar.')
    
    return JsonResponse({'success': False, 'error': 'Método no permitido'})






def estudiantes_por_seccion(request, seccion_id):
    # Obtiene la sección por su ID
    seccion = get_object_or_404(Secciones, id=seccion_id)
    
    # Obtiene todos los estudiantes que pertenecen a esa sección
    estudiantes = Estudiante.objects.filter(seccion=seccion)
    cursos = get_object_or_404(Grado, id=seccion_id)
    grado = get_object_or_404(Grado, id=seccion_id) 
    # Pasa los estudiantes y la sección a la plantilla
    return render(request, 'estudiantes_por_seccion.html', {
        'seccion': seccion,
            'cursos': cursos,
                'aula': grado.aula, 
        'estudiantes': estudiantes
    })

