from django.urls import path
from . import views

urlpatterns = [
    path('', views.clientes),
    path("registrarCliente/", views.registrarCurso),
    path("eliminarCliente/<id>", views.eliminarCurso),
    path("editarCliente/<id>", views.editarCurso),
    path("editarCliente/", views.editar)
]