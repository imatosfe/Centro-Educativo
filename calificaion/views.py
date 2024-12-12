from django.shortcuts import redirect, render

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
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
    seccion = get_object_or_404(Secciones, id=seccion_id)
    estudiante = get_object_or_404(Estudiante, id=estudiante_id)
    asignaturas = obtener_asignaturas_por_grado(seccion.grado)

    if request.method == 'POST':
        form = CalificacionForm(request.POST)
        if form.is_valid():
            for asignatura_id, nota in form.cleaned_data.items():
                if asignatura_id.startswith('nota_'):
                    asignatura_id = int(asignatura_id[5:])
                    asignatura = get_object_or_404(Asignatura, id=asignatura_id)
                    # Validación y guardado de la calificación (como se mostró antes)
            return redirect('listar_estudiantes_calificacion', seccion_id=seccion.id)
    else:
        form = CalificacionForm()

    return render(request, 'agregar_calificacion.html', {
        'seccion': seccion,
        'estudiante': estudiante,
        'asignaturas': asignaturas,
        'form': form,
    })


