from pyexpat.errors import messages
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Aula
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages


# Aulas++



class AulaListView(ListView):
    model = Aula
    template_name = 'aula_list.html'
    context_object_name = 'aulas'  # Para referenciarlo de forma más clara en la plantilla

      
    def get_queryset(self):
        return Aula.objects.all()


class AulaDetailView(DetailView):
    model = Aula
    template_name = 'aula_detail.html'
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from .models import Aula


class AulaCreateView(CreateView):
    model = Aula
    fields = ['nombre']
    template_name = 'aula/aula_form.html'
    success_url = reverse_lazy('aula-list')

    # Sobrescribir form_valid para agregar mensajes de confirmación
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, '¡Aula creada exitosamente!')
        return response

    # Sobrescribir form_invalid para agregar mensajes de error
    def form_invalid(self, form):
        messages.error(self.request, 'Hubo un error al intentar crear el aula.')
        return super().form_invalid(form)


class AulaUpdateView(UpdateView):
    model = Aula
    fields = ['nombre']
    template_name = 'aula/aula_form.html'
    success_url = reverse_lazy('aula-list')

    # Sobrescribir form_valid para agregar mensajes de confirmación
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, '¡Aula actualizada exitosamente!')
        return response

    # Sobrescribir form_invalid para agregar mensajes de error
    def form_invalid(self, form):
        messages.error(self.request, 'Hubo un error al intentar actualizar el aula.')
        return super().form_invalid(form)


class AulaDeleteView(DeleteView):
    model = Aula
    template_name = 'aula_confirm_delete.html'
    success_url = reverse_lazy('aula-list')


@csrf_exempt  # Asegúrate de usar este decorador si no estás enviando el token CSRF.
def eliminar_aula(request, aula_id):
    if request.method == 'POST':
        # Intenta obtener el estudiante por ID
        curso = get_object_or_404(Aula, id=aula_id)
        
        try:
            curso.delete()  # Intenta eliminar el estudiante
            messages.success(request, 'Aula eliminado exitosamente.')
            return JsonResponse({'success': True})
        except Exception as e:
            messages.error(request, 'No se pudo eliminar la Aula.')
            return JsonResponse({'error': str(e)})
    

    return JsonResponse({'success': False, 'error': 'Método no permitido'})