from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'vrxallapp/home.html')

# def detalles_app(request, slug):
#     apps = {
#         'sportmind': {
#             'nombre': 'SportMind',
#             'categoria': 'Deporte',
#             'tipo': 'Destreza',
#             'descripcion': 'Imagina entrenar tu mente...',
#             'imagenes': [
#                 'img/sportmind1.png',
#                 'img/sportmind2.png',
#                 'img/sportmind3.png',
#                 'img/sportmind4.png',
#                 'img/sportmind5.png',
#                 'img/sportmind6.png',
#             ]
#         },
#     }
#     app = apps.get(slug)
#     return render(request, 'detalles_app.html', {'app': app})

def detalles_app(request, slug):
    return render(request, 'vrxallapp/detalles_app.html', {'slug': slug})