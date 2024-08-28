from django.urls import path
from . import views

urlpatterns = [
    path('', views.clientes),
    path("agregarCliente/", views.agregarCliente),
    path("registrarCliente/", views.registrarCliente),
    path("eliminarCliente/<id>", views.eliminarCliente),
    path("editarCliente/<id>", views.editarCliente),
    path("editarCliente/", views.editar)
]