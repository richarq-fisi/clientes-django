from django.shortcuts import render, redirect
from .models import Cliente
from django.contrib import messages

# Create your views here.
def clientes(request):
    clientes = Cliente.objects.all()
    return render(request, "clientes.html", {"clientes": clientes})

def agregarCliente(request):
    clientes = Cliente.objects.all()
    return render(request, "agregarCliente.html", {"clientes": clientes})

def registrarCliente(request):
    nombre = request.POST["txtNombre"]
    email = request.POST["txtEmail"]
    telefono = request.POST["txtTelefono"]
    direccion = request.POST["txtDireccion"]

    cliente = Cliente.objects.create(
        nombre = nombre,
        email = email,
        telefono = telefono,
        direccion = direccion
    )
    return redirect("/")

def eliminarCliente(request, id):
    try:
        cliente = Cliente.objects.get(id=id)
        cliente.delete()
        return redirect("/")  # Asegúrate de devolver un redirect después de eliminar el curso
    except Cliente.DoesNotExist:
        return redirect("/")  # Puedes redirigir a la página principal si el curso no existe

def editarCliente(request, id):
    cliente = Cliente.objects.get(id=id)
    return render(request, "editarCliente.html", {"cliente": cliente})

def editar(request):
    id = request.POST["txtId"]
    nombre = request.POST["txtNombre"]
    email = request.POST["txtEmail"]
    telefono = request.POST["txtTelefono"]
    direccion = request.POST["txtDireccion"]

    cliente = Cliente.objects.get(id=id)
    
    cliente.nombre = nombre
    cliente.email = email
    cliente.telefono = telefono
    cliente.direccion = direccion

    cliente.save()

    return redirect("/")