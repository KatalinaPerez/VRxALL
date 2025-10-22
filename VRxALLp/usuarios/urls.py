from django.urls import path
from . import views  
from django.contrib.auth import views as auth_views
from .views import logout_get_view 

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', logout_get_view, name='logout'),
    path('registro/', views.registro_view, name='registro'),
    path('cuenta/', views.cuenta_view, name='cuenta'),
]