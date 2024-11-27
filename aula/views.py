from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Aula
# Aulas
class AulaListView(ListView):
    model = Aula
    template_name = 'aula_list.html'

class AulaDetailView(DetailView):
    model = Aula
    template_name = 'aula_detail.html'

class AulaCreateView(CreateView):
    model = Aula
    fields = ['nombre']
    template_name = 'aula_form.html'
    success_url = reverse_lazy('aula-list')

class AulaUpdateView(UpdateView):
    model = Aula
    fields = ['nombre']
    template_name = 'aula_form.html'
    success_url = reverse_lazy('aula-list')

class AulaDeleteView(DeleteView):
    model = Aula
    template_name = 'aula_confirm_delete.html'
    success_url = reverse_lazy('aula-list')