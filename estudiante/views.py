from django.shortcuts import render, redirect, get_object_or_404
from .forms import EstudianteForm
from .models import Estudiante
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages



from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def crear_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Estudiante creado con éxito')
                return redirect('lista_estudiantes')
            except Exception as e:
                messages.error(request, f'Error al crear el estudiante: {str(e)}')
    else:
        form = EstudianteForm()

    return render(request, 'crear_estudiante.html', {'form': form , 'estudiantes_form': form,})
 

# @login_required
def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'lista_estudiantes.html', {'estudiantesss': estudiantes})

# @login_required
def editar_estudiante(request, estudiante_id):
    estudiante = get_object_or_404(Estudiante, pk=estudiante_id)
  
    if request.method == 'POST':
        form = EstudianteForm(request.POST, instance=estudiante)
        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'Estudiante actualizado con éxito')
             
                return redirect('lista_estudiantes')
        except Exception as e:
            messages.error(request, f'Error al actualizar el estudiante: {str(e)}')
         
    else:
        form = EstudianteForm(instance=estudiante)
    return render(request, 'crear_estudiante.html', {'form': form})






@csrf_exempt  # Asegúrate de usar este decorador si no estás enviando el token CSRF.
def eliminar_estudiante(request, estudiante_id):
    if request.method == 'POST':
        # Intenta obtener el estudiante por ID
        estudiante = get_object_or_404(Estudiante, id=estudiante_id)
        
        try:
            estudiante.delete()  # Intenta eliminar el estudiante
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    
    return JsonResponse({'success': False, 'error': 'Método no permitido'})




