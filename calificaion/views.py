from django.shortcuts import render

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Aula, Grado, Seccion, Estudiante, Profesor, Asignatura, Calificacion

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
    model = Seccion
    template_name = 'reporte_general.html'
    context_object_name = 'secciones'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grados'] = Grado.objects.all()
        return context

