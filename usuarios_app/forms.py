from django import forms 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import AuthenticationForm
from .models import Usuariohtp



from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import PasswordChangeForm


class CambiarContrasenaForm(PasswordChangeForm):
    old_password = forms.CharField(
        label=_("Contraseña actual"),
        widget=forms.PasswordInput,
        strip=False,
        help_text=_("Ingrese su contraseña actual."),
    )
    new_password1 = forms.CharField(
        label=_("Nueva contraseña"),
        widget=forms.PasswordInput,
        strip=False,
        help_text=_("Ingrese su nueva contraseña."),
    )
    new_password2 = forms.CharField(
        label=_("Confirmar nueva contraseña"),
        widget=forms.PasswordInput,
        strip=False,
        help_text=_("Confirme su nueva contraseña."),
    )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')  # Extraemos el usuario de kwargs
        super().__init__(user, *args, **kwargs)  # Llamamos al constructor de PasswordChangeForm





class EditarPerfilForm(forms.ModelForm):
    class Meta:
        model = Usuariohtp
        fields = ['nombre', 'apellido', 'email', 'telefono', 'direccion', 'imagen', 'username']  # Asegúrate de incluir 'imagen' aquí



        
class FormLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormLogin, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control form-control-user'
        self.fields['password'].widget.attrs['class'] = 'form-control form-control-user'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'
        self.fields['username'].widget.attrs['placeholder'] = 'Usuario'

class FormUsuarioSocio(forms.ModelForm):

    password1 = forms.CharField(label = 'Contraseña',widget = forms.PasswordInput(
        attrs = {
            'class': 'form-control form-control-user',
            'placeholder': 'Contraseña',
            'id': 'password1',
            'required':'required',
        }
    ))

    password2 = forms.CharField(label = 'Contraseña de Confirmación', widget = forms.PasswordInput(
        attrs={
            'class': 'form-control form-control-user',
            'placeholder': 'Repetir Contraseña',
            'id': 'password2',
            'required': 'required',
        }
    ))

    class Meta:
            model = Usuariohtp
            fields = ('email', 'username', 'identificacion', 'nombre', 'apellido', 'telefono', 'direccion', 'imagen', 'usuario_activo', 'usuario_administrador')
            widgets = {
             'usuario_activo': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'role': 'switch',
                'id': 'usuarioActivo',
                'checked': 'checked',  # Añade esto si deseas que aparezca marcado por defecto
            }),
            'usuario_administrador': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'role': 'switch',
                'id': 'usuarioAdministrador',
                 
            }),
                'email': forms.EmailInput(
                    attrs={
                        'class': 'form-control form-control-user',
                        'placeholder': 'Correo Electrónico',
                    }
                ),
                'nombre': forms.TextInput(
                    attrs={
                        'class': 'form-control form-control-user',
                        'placeholder': 'Nombre',
                        'required': 'required'
                    }
                ),
                'apellido': forms.TextInput(
                    attrs={
                        'class': 'form-control form-control-user',
                        'placeholder': 'Apellido',
                        'required': 'required'
                    }                
                ),
                'identificacion': forms.NumberInput(
                    attrs={
                        'class': 'form-control form-control-user',
                        'placeholder': 'Identificación',
                        'required': 'required'
                    }
                ),
                'telefono': forms.NumberInput(
                    attrs={
                        'class': 'form-control form-control-user',
                        'placeholder': 'Teléfono',
                        'required': 'required'
                    }
                ),
                'direccion': forms.TextInput(
                    attrs={
                        'class': 'form-control form-control-user',
                        'placeholder': 'Dirección',
                        'required': 'required'
                    }
                ),
                'username': forms.TextInput(
                    attrs={
                        'class': 'form-control form-control-user',
                        'placeholder': 'Usuario',
                        'required': 'required'
                    }
                )
            }

    def clean_password2(self):
        """ Validación de Contraseña
        Metodo que valida que ambas contraseñas ingresadas sean igual, esto antes de ser encriptadas
        y guardadas en la base dedatos, Retornar la contraseña Válida.
        Excepciones:
        - ValidationError -- cuando las contraseñas no son iguales muestra un mensaje de error
        """
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError('¡Las Contraseñas no coinciden!')
        return password2

    def save(self,commit = True):
        user = super().save(commit = False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

class FormUsuarioFoto(forms.ModelForm):

    class Meta:
        model = Usuariohtp
        fields = ('imagen',)
        widgets = {
            'imagen': forms.FileInput(
                attrs = {
                    'class': 'form-control form-control-user',
                }
            )
        }


class FormUsuarioEditar(UserChangeForm):
    class Meta:
        model = Usuariohtp
        fields = ('email','username','nombre','apellido','telefono','direccion', 'usuario_activo', 'usuario_administrador', 'identificacion', 'imagen'  )
        widgets = {
            'email': forms.EmailInput(
                attrs = {
                    'class': 'form-control form-control-user',
                    'placeholder': 'Correo Electrónico',
                    'label': 'Correo Electrónico',
                      'readonly': 'readonly',  
                }
            ),
            'username': forms.TextInput(
                attrs = {
                    'class': 'form-control form-control-user',
                    'placeholder': 'Usuario',
                    'label': 'Nombre Usuario',
                      'readonly': 'readonly',  
                }
            ),
            'first_name': forms.TextInput(
                attrs = {
                    'class': 'form-control form-control-user',
                    'placeholder': 'Nombre',
                    'label': 'Nombre',
                }
            ),
            'last_name': forms.TextInput(
                attrs = {
                    'class': 'form-control form-control-user',
                    'placeholder': 'Apellido',
                    'label': 'Apellido',
                }
            ),
            'telefono': forms.NumberInput(
                attrs = {
                    'class': 'form-control form-control-user',
                    'placeholder': 'Teléfono',
                    'label': 'Teléfono',
                }
            ),
            'direccion': forms.TextInput(
                attrs = {
                    'class': 'form-control form-control-user',
                    'placeholder': 'Dirección',
                    'label': 'Dirección',
                }
            ),
            'usuario_activo': forms.CheckboxInput(
                attrs = {
                    'class': 'form-control form-control-user',
                    'label': 'Usuario Activo',

                } 
            ),
       
            'usuario_administrador': forms.CheckboxInput(
                attrs = {
                    'class': 'form-control form-control-user',
                    'label': 'Usuario Administrador',

                }
            ),
            'identificacion': forms.NumberInput(
                attrs = {
                    'class': 'form-control form-control-user',
                    'placeholder': 'Identificación',
                
                }   
            ),

        }