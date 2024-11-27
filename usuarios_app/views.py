from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.db.models import Q
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from .models import Usuariohtp
from .forms import FormUsuarioSocio, FormLogin, FormUsuarioFoto,  FormUsuarioEditar
from django.views import View  # Otras importaciones necesarias
from django.contrib import messages
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.decorators import login_required
from .forms import EditarPerfilForm
from django.contrib.auth import update_session_auth_hash



from .forms import CambiarContrasenaForm




@login_required
def cambiar_password(request):
    if request.method == 'POST':
        # Pasamos el usuario y los datos del formulario
        form = CambiarContrasenaForm(user=request.user, data=request.POST)
        if form.is_valid():
            try:
                user = form.save()  # Guarda la nueva contraseña
                update_session_auth_hash(request, user)  # Mantiene la sesión del usuario
                messages.success(request, 'Su contraseña ha sido actualizada con éxito.')
                return redirect('editar_usuario', user_id=request.user.id)  # Redirige a la página de perfil
            except Exception as e:
                # Si ocurre algún error, muestra un mensaje de error
                messages.error(request, f'Error al actualizar la contraseña: {str(e)}')
        else:
            messages.error(request, 'Ha ocurrido un error: las contraseñas proporcionadas no coinciden.')
    else:
        # Si no es POST, inicializamos el formulario
        form = CambiarContrasenaForm(user=request.user)

    # Renderizamos el formulario en la plantilla
    return render(request, 'cambiar_password.html', {'form': form})


class EditarPerfilView(View):
    def get(self, request, user_id, *args, **kwargs):
        user = Usuariohtp.objects.get(id=user_id)
        form = FormUsuarioEditar(instance=user)  # Usa FormUsuarioEditar aquí
        return render(request, 'editar_perfil.html', {'form': form, 'user': user})

    def post(self, request, user_id, *args, **kwargs):
        user = Usuariohtp.objects.get(id=user_id)
        form = FormUsuarioEditar(request.POST, request.FILES, instance=user)
        
        # Manejar los checkboxes
        user.usuario_activo = 'usuario_activo' in request.POST
        user.usuario_administrador = 'usuario_administrador' in request.POST

        if form.is_valid():
            form.save()
            user.save()  # Guarda los cambios realizados a los campos de usuario activo y administrador
            messages.success(request, '¡Usuario actualizado con éxito!')
            return redirect('editar_usuario', user_id=user.id)  # Redirige a la vista de edición
        else:
            messages.error(request, 'Hubo un error al actualizar el usuario. Por favor, revisa los campos.')
        
        return render(request, 'editar_perfil.html', {'form': form, 'user': user})

    




class RegistrarUsuario(CreateView):
    model = Usuariohtp
    form_class = FormUsuarioSocio
    template_name = 'crear_usuario.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)  # Incluye request.FILES para manejar imágenes
        if form.is_valid():
            nuevo_usuario = self.create_usuario(form)
            messages.success(request, 'Usuario Registrado con Éxito')
            return self.handle_successful_registration()
        else:
            self.handle_registration_error(form)
            return render(request, self.template_name, {'form': form})

    def create_usuario(self, form):
        """Crea una nueva instancia de UsuarioSocio a partir del formulario."""
        nuevo_usuario = Usuariohtp(
            identificacion=form.cleaned_data['identificacion'],
            nombre=form.cleaned_data['nombre'],
            apellido=form.cleaned_data['apellido'],
            email=form.cleaned_data['email'],
            username=form.cleaned_data['username'],
            telefono=form.cleaned_data['telefono'],
            direccion=form.cleaned_data['direccion'],
            imagen=form.cleaned_data['imagen']
        )
        nuevo_usuario.set_password(form.cleaned_data['password1'])
        nuevo_usuario.save()
     
        return nuevo_usuario

    def handle_successful_registration(self):
        """Redirige al usuario según el template."""
        if self.template_name == "editar_perfil.html":
            return redirect('editar_usuario')
        else:
            return redirect('crear_usuario')

    def handle_registration_error(self, form):
        """Muestra el formulario con errores y mensajes de error."""
        for field in form:
            for error in field.errors:
                messages.error(self.request, f'Error en {field.label}: {error}')

        for error in form.non_field_errors():
            messages.error(self.request, error)


class Login(FormView):
    template_name = 'login.html'
    form_class = FormLogin

    success_url = reverse_lazy('inicio2')


    @method_decorator(csrf_protect)
    @method_decorator(never_cache)    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
        
           return HttpResponseRedirect(self.get_success_url())
      
       
          
        return super(Login, self).dispatch(request, *args, **kwargs)
    
    def form_valid(self,form):
    
        login(self.request, form.get_user())
       
        return super(Login,self).form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Error al iniciar sesión. Verifique sus credenciales.")
        return super(Login, self).form_invalid(form)    

def logout_usuario(request):
    messages.success(request, 'Sesión Cerrada Correctamente')
    logout(request)

    return redirect ('login')


