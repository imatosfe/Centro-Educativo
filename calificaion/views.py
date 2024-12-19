from django.shortcuts import redirect, render

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from asignatura import models
from .models import    Estudiante,  Asignatura, Calificacion
from grado.models import Grado
from seccion.models import Secciones
from profesor.models import Profesor
# Create your views here.
class CalificacionCreateView(CreateView):
    model = Calificacion
    fields = ['estudiante', 'asignatura', 'nota']
    template_name = 'calificacion_form.html'
    success_url = reverse_lazy('calificacion-list')

class CalificacionListView(ListView):
    model = Calificacion
    template_name = 'calificacion_list.html'
    context_object_name = 'calificaciones'

    def get_queryset(self):
        # Filtrar por estudiante, si es necesario
        estudiante_id = self.request.GET.get('estudiante')
        if estudiante_id:
            return Calificacion.objects.filter(estudiante__id=estudiante_id)
        return super().get_queryset()

class CalificacionDetailView(DetailView):
    model = Calificacion
    template_name = 'calificacion_detail.html'
    context_object_name = 'calificacion'

class CalificacionDeleteView(DeleteView):
    model = Calificacion
    template_name = 'calificacion_confirm_delete.html'
    success_url = reverse_lazy('calificacion-list')



class ReporteCalificacionesPorEstudianteView(ListView):
    model = Calificacion
    template_name = 'reporte_calificaciones.html'
    context_object_name = 'calificaciones'

    def get_queryset(self):
        estudiante_id = self.kwargs.get('estudiante_id')
        return Calificacion.objects.filter(estudiante__id=estudiante_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        estudiante = Estudiante.objects.get(id=self.kwargs.get('estudiante_id'))
        context['estudiante'] = estudiante
        return context




class ReporteGeneralView(ListView):
    model = Secciones
    template_name = 'reporte_general.html'
    context_object_name = 'secciones'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grados'] = Grado.objects.all()
        return context









def listar_secciones(request):
    secciones = Secciones.objects.all()  # Obtener todas las secciones
    return render(request, 'listar_secciones.html', {
        'secciones': secciones,
    })






# views.py
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .forms import CalificacionForm
from seccion.models import Secciones
from estudiante.models import Estudiante
from asignatura.models import Asignatura

from django.db.models import Avg

def obtener_asignaturas_por_grado(grado):
    return Asignatura.objects.filter(grado=grado)

def listar_estudiantes_calificacion(request, seccion_id):
    seccion = get_object_or_404(Secciones, id=seccion_id)
    estudiantes = Estudiante.objects.filter(seccion=seccion) \
                                  .annotate(promedio=Avg('calificaciones__nota'))

    asignaturas = obtener_asignaturas_por_grado(seccion.grado)

    return render(request, 'listar_estudiantes_calificacion.html', {
        'seccion': seccion,
        'estudiantes': estudiantes,
        'asignaturas': asignaturas,
    })

def agregar_calificacion(request, seccion_id, estudiante_id):
    # Obtener la sección y el estudiante
    seccion = get_object_or_404(Secciones, pk=seccion_id)
    estudiante = get_object_or_404(Estudiante, pk=estudiante_id)
    
    # Obtener las asignaturas relacionadas con el grado de la sección
    asignaturas = Asignatura.objects.filter(grado=seccion.grado)
    grado = seccion.grado  # Esto nos da el grado de la sección

        # Obtener el aula asociado al grado
    aula = grado.aula 
    # Preparar datos iniciales si hay calificaciones existentes
    initial_data = {}
    if request.method == 'GET':
        for asignatura in asignaturas:
            try:
                calificacion = Calificacion.objects.get(estudiante=estudiante, asignatura=asignatura)
                initial_data[f'nota_{asignatura.id}'] = calificacion.nota
            except Calificacion.DoesNotExist:
                initial_data[f'nota_{asignatura.id}'] = None

        form = CalificacionForm(seccion=seccion, initial=initial_data)

    elif request.method == 'POST':
        form = CalificacionForm(request.POST, seccion=seccion)
        if form.is_valid():
            # Guardar las calificaciones
            for asignatura in asignaturas:
                nota = form.cleaned_data.get(f'nota_{asignatura.id}')
                if nota is not None:
                    # Crear o actualizar la calificación
                    calificacion, created = Calificacion.objects.update_or_create(
                        estudiante=estudiante,
                        asignatura=asignatura,
                     grado=grado,
                        defaults={'nota': nota}
                    )
            # Redirigir después de guardar todas las calificaciones
            return redirect('listar_estudiantes_calificacion', seccion_id=seccion_id)

    # Renderizar el formulario en GET o si hay errores en el POST
    return render(request, 'agregar_calificacion.html', {
        'form': form,
        'asignaturas': asignaturas,
        'estudiante': estudiante,
        'seccion': seccion,
    })



def get_calificaciones(estudiante, asignaturas):
    """Obtiene las calificaciones de un estudiante para las asignaturas dadas."""
    calificaciones = {}
    for asignatura in asignaturas:
        try:
            calificacion = Calificacion.objects.get(estudiante=estudiante, asignatura=asignatura)
            calificaciones[f'nota_{asignatura.id}'] = calificacion.nota
        except Calificacion.DoesNotExist:
            calificaciones[f'nota_{asignatura.id}'] = None  # Si no tiene calificación, lo dejamos en blanco
    print("Calificaciones obtenidas:", calificaciones)  # Esto te ayudará a verificar
    return calificaciones




from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Estudiante, Grado

def promocionar_estudiante(request, estudiante_id, nuevo_grado_id):
    estudiante = get_object_or_404(Estudiante, id=estudiante_id)
    nuevo_grado = get_object_or_404(Grado, id=nuevo_grado_id)

    if estudiante.grado_actual == nuevo_grado:
        messages.warning(request, "El estudiante ya está en este grado.")
    else:
        estudiante.grado_actual = nuevo_grado
        estudiante.save()
        messages.success(request, f"El estudiante {estudiante.nombre} fue promovido a {nuevo_grado.nombre}.")
    
    return redirect('listar_estudiantes')  # Ajusta la redirección según tu sistema


from django.shortcuts import render
from .models import Estudiante, Calificacion
from django.db.models import Avg


from django.db.models import Avg
from django.shortcuts import render, get_object_or_404
from .models import Estudiante, Calificacion

def calificaciones_por_grado(request, estudiante_id):
    # Obtener al estudiante por su ID
    estudiante = get_object_or_404(Estudiante, id=estudiante_id)

    # Obtener las calificaciones del estudiante
    calificaciones = Calificacion.objects.filter(estudiante=estudiante).order_by('grado', 'asignatura')

    # Obtener el grado del estudiante
    grado = estudiante.seccion.grado 

    # Crear un diccionario para almacenar los promedios por grado
    promedios_por_grado = {}

    # Filtrar calificaciones por grado
    calificaciones_grado = calificaciones.filter(grado=grado)

    # Calcular el promedio de calificaciones por grado
    promedio = calificaciones_grado.aggregate(promedio=Avg('nota'))['promedio']

    # Almacenar el promedio por grado en el diccionario
    promedios_por_grado[grado] = promedio

    # Retornar la respuesta renderizada
    return render(request, 'calificaciones_por_grado.html', {
        'estudiante': estudiante,
        'calificaciones': calificaciones,
        'promedios_por_grado': promedios_por_grado,
    })

