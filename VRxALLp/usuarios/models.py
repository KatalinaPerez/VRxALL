from django.contrib.auth.models import User
from django.db import models

class Perfil(models.Model):
    GENERO_CHOICES = [
        ('F', 'Femenino'),
        ('M', 'Masculino'),
        ('NB', 'No binario'),
        ('ND', 'Prefiero no decirlo'),
        ('O', 'Otro'),
    ]

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    edad = models.PositiveIntegerField()
    genero = models.CharField(max_length=10, choices=GENERO_CHOICES)
    proyecto_descarga = models.CharField(max_length=100)

    def __str__(self):
        return self.usuario.username

# Create your models here.
