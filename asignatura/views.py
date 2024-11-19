from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Aula, Grado, Seccion, Estudiante, Profesor, Asignatura, Calificacion

# Create your views here.
# Asignaturas
class AsignaturaListView(ListView):
    model = Asignatura
    template_name = 'asignatura_list.html'

class AsignaturaDetailView(DetailView):
    model = Asignatura
    template_name = 'asignatura_detail.html'

class AsignaturaCreateView(CreateView):
    model = Asignatura
    fields = ['nombre', 'grado', 'profesor']
    template_name = 'asignatura_form.html'
    success_url = reverse_lazy('asignatura-list')

class AsignaturaUpdateView(UpdateView):
    model = Asignatura
    fields = ['nombre', 'grado', 'profesor']
    template_name = 'asignatura_form.html'
    success_url = reverse_lazy('asignatura-list')

class AsignaturaDeleteView(DeleteView):
    model = Asignatura
    template_name = 'asignatura_confirm_delete.html'
    success_url = reverse_lazy('asignatura-list')
