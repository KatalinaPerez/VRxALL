from django import forms
from django.contrib.auth.models import User
from .models import Perfil
import re

class RegistroForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Contraseña")
    confirmar_password = forms.CharField(widget=forms.PasswordInput, label="Confirmar Contraseña")

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    edad = forms.IntegerField(min_value=13, label="Edad")
    genero = forms.ChoiceField(choices=Perfil.GENERO_CHOICES)
    proyecto_descarga = forms.ChoiceField(choices=[
        ('SportMind', 'SportMind'),
        ('NeuroFlex', 'NeuroFlex'),
        ('EmotionLab', 'EmotionLab'),
        ('AcVR', 'AcVR'),
    ])

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 6 or not re.search(r'[A-Z]', password) or not re.search(r'[\W_]', password):
            raise forms.ValidationError("La contraseña debe tener al menos 6 caracteres, una mayúscula y un símbolo.")
        return password

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirmar = cleaned_data.get("confirmar_password")
        if password != confirmar:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return cleaned_data
