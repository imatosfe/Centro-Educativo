from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Aula, Grado, Seccion, Estudiante, Profesor, Asignatura, Calificacion

# Create your views here.
class SeccionListView(ListView):
    model = Seccion
    template_name = 'seccion_list.html'

class SeccionDetailView(DetailView):
    model = Seccion
    template_name = 'seccion_detail.html'

class SeccionCreateView(CreateView):
    model = Seccion
    fields = ['nombre', 'grado']
    template_name = 'seccion_form.html'
    success_url = reverse_lazy('seccion-list')

class SeccionUpdateView(UpdateView):
    model = Seccion
    fields = ['nombre', 'grado']
    template_name = 'seccion_form.html'
    success_url = reverse_lazy('seccion-list')

class SeccionDeleteView(DeleteView):
    model = Seccion
    template_name = 'seccion_confirm_delete.html'
    success_url = reverse_lazy('seccion-list')