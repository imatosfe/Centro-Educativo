from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Aula, Grado, Seccion, Estudiante, Profesor, Asignatura, Calificacion

# Create your views here.
class EstudianteListView(ListView):
    model = Estudiante
    template_name = 'estudiante_list.html'

class EstudianteDetailView(DetailView):
    model = Estudiante
    template_name = 'estudiante_detail.html'

class EstudianteCreateView(CreateView):
    model = Estudiante
    fields = ['nombre', 'apellido', 'seccion']
    template_name = 'estudiante_form.html'
    success_url = reverse_lazy('estudiante-list')

class EstudianteUpdateView(UpdateView):
    model = Estudiante
    fields = ['nombre', 'apellido', 'seccion']
    template_name = 'estudiante_form.html'
    success_url = reverse_lazy('estudiante-list')

class EstudianteDeleteView(DeleteView):
    model = Estudiante
    template_name = 'estudiante_confirm_delete.html'
    success_url = reverse_lazy('estudiante-list')