from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import RegistroForm
from .models import Perfil
import smtplib
from email.mime.text import MIMEText

def login_view(request):
    
    # Si el método de la petición es POST, significa que el usuario envió el formulario
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        # Verificamos si el formulario es válido
        if form.is_valid():
            # Si es válido, obtenemos el usuario
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            
            # Si el usuario existe y las credenciales son correctas
            if user is not None:
                # Iniciamos la sesión para ese usuario
                login(request, user)
                messages.info(request, f"Has iniciado sesión como {username}.")
                # Redirigimos a la página principal (o a donde quieras)
                return redirect('home') # 'home' es el 'name' de la URL a la que quieres ir
            else:
                # Si las credenciales son incorrectas
                messages.error(request, "Usuario o contraseña incorrectos.")
        else:
            # Si el formulario no es válido
            messages.error(request, "Usuario o contraseña incorrectos.")
            
    # Si la petición es GET (el usuario acaba de llegar a la página), creamos un formulario vacío
    form = AuthenticationForm()
    # Renderizamos la plantilla HTML pasándole el formulario como contexto
    return render(request, 'usuarios/login.html', {'form': form})


def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            Perfil.objects.create(
                usuario=user,
                edad=form.cleaned_data['edad'],
                genero=form.cleaned_data['genero'],
                proyecto_descarga=form.cleaned_data['proyecto_descarga']
            )

            # Enviar correo de bienvenida
            enviar_bienvenida(user.email, user.first_name)

            messages.success(request, 'Registro exitoso. ¡Bienvenido a VR x ALL!')
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'usuarios/registro.html', {'form': form})

def logout_get_view(request):
    logout(request)
    # Redirigimos a la página principal
    return redirect('home')

def cuenta_view(request):
    return render(request, 'usuarios/cuenta.html')
