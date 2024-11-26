from django.forms import ModelForm
from django import forms
from .models import Usuario

class UsuarioModelForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['email', 'nombre_usuario', 'password', 'bio', 'ciudad', 'fecha_nac', 'foto_perfil']
        labels = '__all__'
        
        """{
            'email': ('Tu email'),
            'nombre_usuario': ('Nombre de usuario'),
            'password': ('Contraseña'),
            'bio': ('Tu biografía'),
            'ciudad': ('Ciudad'),
            'fecha_nac': ('foto_perfil')   
        }"""
        
        help_texts = {
            'email': ('100 caracteres como máximo'),
            'nombre_usuario': ('100 caracteres como máximo'),
            'password': ('100 caracteres como máximo'),
            'ciudad': ('150 caracteres como máximo')    
        }
        widgets = {
            'bio': forms.Textarea(attrs={
                'class': 'bio',
                'placeholder': 'Escribe aquí tu descripción...',
                'rows': 4,
                'cols': 50,
            }),
            'fecha_nac': forms.SelectDateWidget()
            
        }
        localized_fields = ['fecha_nac']
        
        # Validación para verificar si el nombre de usuario ya existe
    def clean_nombre_usuario(self):
        nombre_usuario = self.cleaned_data.get('nombre_usuario')
        if Usuario.objects.filter(nombre_usuario=nombre_usuario).exists():
            raise forms.ValidationError('El nombre de usuario ya está en uso. Por favor, elige otro.')
        return nombre_usuario

    # Validación para verificar si el email ya existe
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Usuario.objects.filter(email=email).exists():
            raise forms.ValidationError('El email ya está registrado. Por favor, utiliza otro.')
        return email
