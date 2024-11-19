from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Aula, Grado, Seccion, Estudiante, Profesor, Asignatura, Calificacion


class GradoListView(ListView):
    model = Grado
    template_name = 'grado_list.html'

class GradoDetailView(DetailView):
    model = Grado
    template_name = 'grado_detail.html'

class GradoCreateView(CreateView):
    model = Grado
    fields = ['nombre', 'aula']
    template_name = 'grado_form.html'
    success_url = reverse_lazy('grado-list')

class GradoUpdateView(UpdateView):
    model = Grado
    fields = ['nombre', 'aula']
    template_name = 'grado_form.html'
    success_url = reverse_lazy('grado-list')

class GradoDeleteView(DeleteView):
    model = Grado
    template_name = 'grado_confirm_delete.html'
    success_url = reverse_lazy('grado-list')