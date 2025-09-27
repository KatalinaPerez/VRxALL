from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'vrxallapp/home.html')

def detalles_app(request, slug):
    apps = {
        'sportmind': {
            'nombre': 'SportMind',
            'categoria': 'Deporte',
            'tipo': 'Destreza',
            'edades':'Contenido es apto para todas las edades',
            'candado':'Esta aplicación recopilará y almacenará tu información y datos de progreso, incluyendo tu nombre de usuario, para optimizar tu experiencia y contribuir a mejoras futuras.',
            'descripcion': 'Imagina entrenar tu mente...',
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
                'img/neuroflex2.png',
                'img/neuroflex3.png',
                'img/neuroflex4.png',
                'img/neuroflex5.png',
                'img/neuroflex6.png',
            ]
        },
    }
    app = apps.get(slug)
    return render(request, 'vrxallapp/detalles_app.html', {'app': app})
