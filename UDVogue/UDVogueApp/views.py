from django.shortcuts import render
from .models import Editorial, Revista, Producto
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.

def index(request):
    return HttpResponse('primera vista')

def listaEditoriales(request):
    editoriales = Editorial.objects.order_by('nombre')
    nombre_editoriales = ', '.join([editorial.nombre for editorial in editoriales])
    return HttpResponse(nombre_editoriales)

def detalleEDITORIAL(request, id_editorial):
    try:
        editorial = Editorial.objects.get(pk=id_editorial) 
        revistas = editorial.revistas.all()

        cadenaTxt = f"{editorial.nombre} - Contacto: {editorial.contacto}\n"

        if revistas.exists():
            cadenaTxt += "Revistas:\n"
            for revista in revistas:
                cadenaTxt += f"- {revista.titulo}, Fecha Publicación: {revista.fecha_publi}, Nº Edición: {revista.numero_edicion}\n"
        else:
            cadenaTxt += "No hay revistas asociadas a esta editorial."
            
        return HttpResponse(cadenaTxt)

    except Editorial.DoesNotExist:
        return HttpResponseNotFound("Editorial no encontrada")

def listaProductos(request):
    productos = Producto.objects.order_by('nombre_producto')
    nombre_productos = ', '.join([producto.nombre_producto for producto in productos])
    return HttpResponse(nombre_productos)