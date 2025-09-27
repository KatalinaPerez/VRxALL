from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('aplicaciones/<slug:slug>/', views.detalles_app, name='detalles_app'),
]