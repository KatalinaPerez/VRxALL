from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home')  # Esto apunta a home.html
]