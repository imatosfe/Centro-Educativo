from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Asignatura
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import AsignaturaForm
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Create your views here.
# Asignaturas
def lista_asignatura(request):
    asign = Asignatura.objects.all()
    return render(request, 'asignatura/asignatura_list.html', {'asignaturas': asign})


class AsignaturaDetailView(DetailView):
    model = Asignatura
    template_name = 'asignatura_detail.html'

class AsignaturaCreateView(CreateView):
    model = Asignatura
    fields = ['nombre', 'grado', 'profesor']
    template_name = 'asignatura_form.html'
    success_url = reverse_lazy('asignatura-list')



def crear_asignatura(request):
    if request.method == 'POST':
        form = AsignaturaForm(request.POST)
        if form.is_valid():
            nombre_curso = form.cleaned_data['nombre']
            if Asignatura.objects.filter(nombre=nombre_curso).exists():
                messages.error(request, f'La Asignatura "{nombre_curso}" ya existe.')
            else:
                form.save()
                messages.success(request, 'Asignatura creada con éxito.')
                return redirect('asignatura-list')  # Redirige a 'asignatura_list' correctamente
        else:
            messages.error(request, 'Error al crear Asignatura.')
    else:
        form = AsignaturaForm()
    return render(request, 'asignatura/asignatura_form.html', {'form': form})




class AsignaturaUpdateView(UpdateView):
    model = Asignatura
    fields = ['nombre', 'grado', 'profesor']
    template_name = 'asignatura_form.html'
    success_url = reverse_lazy('asignatura-list')

class AsignaturaDeleteView(DeleteView):
    model = Asignatura
    template_name = 'asignatura_confirm_delete.html'
    success_url = reverse_lazy('asignatura-list')





def actualizar_asignatura(request, asignatura_id):
    asignatura = get_object_or_404(Asignatura, id=asignatura_id)
    if request.method == 'POST':
        form = AsignaturaForm(request.POST, instance=asignatura)
        if form.is_valid():
            form.save()
            messages.success(request, 'La asignatura ha sido actualizada con éxito.')
            return redirect('asignatura-list')
        else:
            messages.error(request, 'Error al actualizar la asignatura.')
    else:
        form = AsignaturaForm(instance=asignatura)
    return render(request, 'asignatura/asignatura_form.html', {'form': form})




@csrf_exempt
def eliminar_asignatura(request, asignatura_id):
    if request.method == 'POST':
        # Intenta obtener la asignatura por ID
        asignatura = get_object_or_404(Asignatura, id=asignatura_id)
        
        try:
            asignatura.delete()  # Intenta eliminar la asignatura
            messages.success(request, 'Asignatura eliminada exitosamente.')
            return JsonResponse({'success': True})
        except Exception as e:
            messages.error(request, 'Error al eliminar la asignatura.')
            return JsonResponse({'success': False, 'error': str(e)})
    else:
        messages.error(request, 'Método no permitido.')
    
    return JsonResponse({'success': False, 'error': 'Método no permitido'})