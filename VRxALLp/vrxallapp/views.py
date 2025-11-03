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
            'descripcion': 'Imagina entrenar tu mente en un mundo que pone a prueba tu calma interior.\n\n'
            'En SportMind, te enfrentarás a desafíos de realidad virtual que combinan cuerpo y mente: desde mantener el pulso firme en un tiro al blanco hasta controlar tus emociones en plena escalada.\n\n'
            'Mientras tu frecuencia cardíaca y reacciones emocionales se hacen visibles, un avatar guía estará contigo, dándote apoyo, contención y estrategias para superar cada reto...',
            'imagenes': [
                'img/neuroflex1.png',
                'img/neuroflex2.png',
                'img/neuroflex3.png',
                'img/neuroflex4.png',
                'img/neuroflex5.png',
                'img/neuroflex6.png',
            ]
        },
        'emotionlab': {
            'nombre': 'EmotionLab',
            'categoria': 'Cognitivo',
            'tipo': 'Estimulación',
            'edades':'Contenido es apto para todas las edades',
            'candado':'Esta aplicación recopilará y almacenará tu información y datos de progreso, incluyendo tu nombre de usuario, para optimizar tu experiencia y contribuir a mejoras futuras.',
            'descripcion': (
                "Imagina enfrentarte a una exposición sin miedo, en un entorno diseñado para retarte y ayudarte a crecer.\n\n"
                "En EmotionLab, vivirás una experiencia de realidad virtual donde podrás practicar hablar en público eligiendo tu propia presentación y el escenario donde exponer: "
                "una sala de clases llena de estudiantes o la oficina de un profesor, para esos momentos imprevistos donde la exposición ocurre fuera de horario.\n\n"
                "Durante la experiencia, se presentarán distintas situaciones estresantes, como fallas técnicas en el proyector, ruidos molestos o interrupciones inesperadas, "
                "para que aprendas a mantener la calma, adaptarte y continuar con confianza.\n\n"
                "A lo largo de toda la exposición, un robot guía estará contigo, ofreciéndote tips, recordatorios de respiración y apoyo emocional para ayudarte a recuperar el equilibrio "
                "y mantener la calma frente a cualquier obstáculo.\n\n"
                "EmotionLab no solo busca que mejores tus habilidades comunicativas, sino también que desarrolles resiliencia emocional frente a cualquier desafío del mundo real."
            ),
            'imagenes': [
                'img/neuroflex1.png', #hay que cambiar las imágenes
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
