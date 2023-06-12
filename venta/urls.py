from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('clientes/', views.clientes, name='clientes'),
    path('productos/', views.productos, name='productos'),
    path('ventas/', views.ventas, name='ventas'),
    path('seguimiento/', views.seguimiento, name='seguimiento'),
    path('reporte/', views.reporte, name='reporte'),
]
