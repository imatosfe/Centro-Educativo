from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
# cursos/views.py
from django.shortcuts import render, get_object_or_404, redirect

from aula.models import Aula
from .models import Grado
from .forms import CursoForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# @login_required
def lista_cursos(request):
    cursos = Grado.objects.all()
    return render(request, 'grado/lista_cursos.html', {'cursos': cursos})



def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            nombre_curso = form.cleaned_data['nombre']
            # Verificar si el curso ya existe
            if Grado.objects.filter(nombre=nombre_curso).exists():
                messages.error(request, f'El curso "{nombre_curso}" ya existe.')
            else:
                form.save()
                messages.success(request, 'Curso creado con éxito.')
                return redirect('lista_cursos')  # Asegúrate de que la URL sea correcta
        else:
            messages.error(request, 'Error al crear curso.')
    else:
        form = CursoForm()
    return render(request, 'grado/crear_curso.html', {'form': form})



# @login_required
def detalle_curso(request, curso_id):
    curso = get_object_or_404(Grado, id=curso_id)
    return render(request, 'grado/detalle_curso.html', {'curso': curso})

# @login_required
def editar_curso(request, curso_id):  # Debe coincidir con la URL
    curso = get_object_or_404(Grado, id=curso_id)
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            messages.success(request, 'Curso editado con éxito.')
            return redirect('lista_cursos')
        else:
            messages.error(request, 'Error al editar el curso.')
    else:
        form = CursoForm(instance=curso)
    return render(request, 'grado/crear_curso.html', {'form': form})




# @login_required
@csrf_exempt  # Asegúrate de usar este decorador si no estás enviando el token CSRF.
def eliminar_curso(request, curso_id):
    if request.method == 'POST':
        # Intenta obtener el estudiante por ID
        curso = get_object_or_404(Grado, id=curso_id)
        
        try:
            curso.delete()  # Intenta eliminar el estudiante
            messages.success(request, 'Curso eliminado exitosamente.')
            return JsonResponse({'success': True})
        except Exception as e:
            messages.success(request, 'Error al eliminar Curso.')
            return JsonResponse({'success': False, 'error': str(e)})
    
    return JsonResponse({'success': False, 'error': 'Método no permitido'})




from django.shortcuts import render, get_object_or_404
from grado.models import Grado  # Asegúrate de importar Grado
from seccion.models import Secciones  # Asegúrate de importar Secciones



def secciones_por_aula(request, aula_id):
    # Obtener el grado
    grado = get_object_or_404(Grado, id=aula_id)
    
    # Obtener las secciones asociadas a este grado
    seccio = Secciones.objects.filter(grado=grado)
    
    return render(request, 'grado/secciones_por_aula.html', {
        'grado': grado,
        'secciones': seccio,
          'aula': grado.aula, 
    })