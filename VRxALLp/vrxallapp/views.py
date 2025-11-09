from django.shortcuts import render

# --- PASO 1: Mueve el diccionario 'apps' aquí arriba ---
# Así, ambas funciones pueden acceder a él.
apps = {
    'sportmind': {
        'nombre': 'SportMind',
        'categoria': 'Deporte',
        'tipo': 'Destreza',
        'edades':'Contenido es apto para todas las edades',
        'candado':'Esta aplicación recopilará y almacenará tu información y datos de progreso, incluyendo tu nombre de usuario, para optimizar tu experiencia y contribuir a mejoras futuras.',
        'descripcion': 'Imagina entrenar tu mente en un mundo que pone a prueba tu calma interior. '
                       'En SportMind, te enfrentarás a desafíos de realidad virtual que combinan cuerpo y mente: desde mantener el pulso firme en un tiro al blanco hasta controlar tus emociones en plena escalada. Mientras tu frecuencia cardíaca y reacciones emocionales se hacen visibles, un avatar guía estará contigo, dándote apoyo, contención y estrategias para superar cada reto...',
        'imagenes': [
            'img/sportmind1.png',
            'img/sportmind2.png',
            'img/sportmind3.png',
            'img/sportmind4.png',
            'img/sportmind5.png',
            'img/sportmind6.png',
        ]
    },
    'neuroflex': {
        'nombre': 'NeuroFlex',
        'categoria': 'Deporte',
        'tipo': 'Destreza',
        'edades':'Contenido es apto para todas las edades',
        'candado':'Esta aplicación recopilará y almacenará tu información y datos de progreso, incluyendo tu nombre de usuario, para optimizar tu experiencia y contribuir a mejoras futuras.',
        'descripcion': 'Imagina entrenar tu mente...',
        'imagenes': [
            'img/neuroflex1.png',
            # ... (etc)
        ]
    },
    'emotionlab': {
        'nombre': 'EmotionLab', # ¡Ojo! Aquí decía NeuroFlex, lo corregí.
        'categoria': 'Deporte',
        'tipo': 'Destreza',
        'edades':'Contenido es apto para todas las edades',
        'candado':'Esta aplicación recopilará y almacenará tu información y datos de progreso, incluyendo tu nombre de usuario, para optimizar tu experiencia y contribuir a mejoras futuras.',
        'descripcion': 'Imagina entrenar tu mente...',
        'imagenes': [
            'img/emotionlab.png',
            # ... (etc)
        ]
    },
    'acvr': {
        'nombre': 'AcVR', # ¡Ojo! Aquí decía NeuroFlex, lo corregí.
        'categoria': 'Deporte',
        'tipo': 'Destreza',
        'edades':'Contenido es apto para todas las edades',
        'candado':'Esta aplicación recopilará y almacenará tu información y datos de progreso, incluyendo tu nombre de usuario, para optimizar tu experiencia y contribuir a mejoras futuras.',
        'descripcion': 'Imagina entrenar tu mente...',
        'imagenes': [
            'img/acvr.png',
            # ... (etc)
        ]
    },
}

# --- PASO 2: Modifica tu vista 'home' ---
def home(request):
    # Pasa el diccionario 'apps' al contexto del template
    context = {
        'apps': apps
    }
    return render(request, 'vrxallapp/home.html', context)

# --- PASO 3: Simplifica tu vista 'detalles_app' ---
def detalles_app(request, slug):
    # Obtiene la app específica del diccionario global
    app = apps.get(slug)
    return render(request, 'vrxallapp/detalles_app.html', {'app': app})