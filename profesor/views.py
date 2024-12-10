from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Profesor
from .forms import ProfesorForm

#@method_decorator(login_required, name='dispatch')
class ProfesorListView(ListView):
    model = Profesor
    template_name = 'profesores/lista_profesores.html'
    context_object_name = 'profesores'

#@method_decorator(login_required, name='dispatch')
# Vista para crear un nuevo profesor
class ProfesorCreateView(CreateView):
    model = Profesor
    form_class = ProfesorForm
    template_name = 'profesores/form_profesor.html'
    messages.success
    success_url = reverse_lazy('lista_profesores')

    def form_valid(self, form):
        messages.success(self.request, 'El profesor ha sido creado con éxito.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Error al crear el profesor. Por favor, revisa los datos ingresados.')
        return super().form_invalid(form)

#@method_decorator(login_required, name='dispatch')
# Vista para actualizar un profesor existente
class ProfesorUpdateView(UpdateView):
    model = Profesor
    form_class = ProfesorForm
    template_name = 'profesores/form_profesor.html'
    success_url = reverse_lazy('lista_profesores')

    def form_valid(self, form):
        messages.success(self.request, 'El profesor ha sido actualizado con éxito.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Error al actualizar el profesor. Por favor, revisa los datos ingresados.')
        return super().form_invalid(form)

#@method_decorator(login_required, name='dispatch')
# Vista para eliminar un profesor
class ProfesorDeleteView(DeleteView):
    model = Profesor
    template_name = 'profesores/confirmar_eliminar_profesor.html'
    success_url = reverse_lazy('lista_profesores')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'El profesor ha sido eliminado con éxito.')
        return super().delete(request, *args, **kwargs)



@csrf_exempt  # Asegúrate de usar este decorador si no estás enviando el token CSRF.
def eliminar_profesor(request, profesor_id):
    if request.method == 'POST':
        profesor = get_object_or_404(Profesor, id=profesor_id)
        
        try:
            profesor.delete()  # Intenta eliminar el profesor
            messages.success(request, 'El profesor ha sido eliminado con éxito.')  # Mensaje de éxito
            return JsonResponse({'success': True})
        except Exception as e:
            messages.error(request, 'Error al eliminar el profesor: ' + str(e))  # Mensaje de error
            return JsonResponse({'success': False, 'error': str(e)})
    else:
        messages.error(request, 'Error al eliminar el profesor: ' + str(e))  # Mensaje de error
    
    return JsonResponse({'success': False, 'error': 'Método no permitido'})