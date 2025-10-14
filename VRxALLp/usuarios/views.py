from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages

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
        # Cuando el usuario envía el formulario...
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Si el formulario es válido, Django crea el usuario automáticamente
            user = form.save()
            # Mostramos un mensaje de éxito
            messages.success(request, '¡Cuenta creada exitosamente! Ya puedes iniciar sesión.')
            # Redirigimos al usuario a la página de login
            return redirect('login')
        else:
            # Si el formulario no es válido, se mostrarán los errores en la plantilla
            # (ej: las contraseñas no coinciden, el usuario ya existe, etc.)
            messages.error(request, 'Hubo un error en el registro. Por favor, revisa los datos.')
    else:
        # Si el usuario solo está visitando la página, le mostramos un formulario vacío
        form = UserCreationForm()
        
    return render(request, 'usuarios/registro.html', {'form': form})

def logout_get_view(request):
    logout(request)
    # Redirigimos a la página principal
    return redirect('home')