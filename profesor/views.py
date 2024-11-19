from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Aula, Grado, Seccion, Estudiante, Profesor, Asignatura, Calificacion


# Create your views here.

# Profesores
class ProfesorListView(ListView):
    model = Profesor
    template_name = 'profesor_list.html'

class ProfesorDetailView(DetailView):
    model = Profesor
    template_name = 'profesor_detail.html'

class ProfesorCreateView(CreateView):
    model = Profesor
    fields = ['nombre', 'apellido', 'email']
    template_name = 'profesor_form.html'
    success_url = reverse_lazy('profesor-list')

class ProfesorUpdateView(UpdateView):
    model = Profesor
    fields = ['nombre', 'apellido', 'email']
    template_name = 'profesor_form.html'
    success_url = reverse_lazy('profesor-list')

class ProfesorDeleteView(DeleteView):
    model = Profesor
    template_name = 'profesor_confirm_delete.html'
    success_url = reverse_lazy('profesor-list')
