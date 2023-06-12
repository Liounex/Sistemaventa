from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Usuario


def login(request):
    return render(request, 'login.html')


def home(request):
    return render(request, 'home.html')

# Vista Usuarios Nota=> Cambiar de clientes a usuarios


def clientes(request):
    # Inicializamos una variable trayendo los datos de la tabla usuario
    datos_usuario = Usuario.objects.all()
    # excepciones
    try:
        # Codigo para subir los datos del formulario a la base datos
        if request.method == 'POST':
            nombre = request.POST['nombre']
            apellido = request.POST['apellido']
            correo = request.POST['correo']
            direccion = request.POST['direccion']
            telefono = request.POST['telefono']
            usuario = request.POST['usuario']
            contrasena = request.POST['contrasena']
            rol = request.POST['rol']

            usuario = Usuario(nombre=nombre, apellido=apellido, correo=correo, direccion=direccion,
                              telefono=telefono, usuario=usuario, contrasena=contrasena, rol=rol)
            usuario.save()
            # mensaje de alerta en caso salio bien
            messages.success(request, '¡Usuario registrado exitosamente!')

            # Obtén los datos del usuario
            # datos_usuario = Usuario.objects.get(usuario=request.POST['usuario'])
            # Obtén los datos existentes de la base de datos
            datos_usuario = Usuario.objects.all()
            return render(request, 'clientes.html', {'datos_usuario': datos_usuario})
    except:
        messages.error(request, '¡Usuario no registrado!')
    return render(request, 'clientes.html', {'datos_usuario': datos_usuario})


def productos(request):
    return render(request, 'productos.html')


def ventas(request):
    return render(request, 'ventas.html')


def seguimiento(request):
    return render(request, 'seguimiento.html')


def reporte(request):
    return render(request, 'reporte.html')
