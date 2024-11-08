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

def detalleProducto(request, id_producto):
    try:
        producto = Producto.objects.get(pk=id_producto)
        cadenaTxt = f"Producto: {producto.nombre_producto}\nDescripción: {producto.descripcion}\nPrecio: {producto.precio}\n"
        return HttpResponse(cadenaTxt)
    except Producto.DoesNotExist:
        return HttpResponseNotFound("Producto no encontrado")

def listaRevistas(request):
    revistas = Revista.objects.order_by('titulo')
    nombre_revistas = ', '.join([revista.titulo for revista in revistas])
    return HttpResponse(nombre_revistas)

def detalleRevista(request, id_revista):
    try:
        revista = Revista.objects.get(pk=id_revista)
        editorial = revista.editorial
        cadenaTxt = f"Revista: {revista.titulo}\nFecha de Publicación: {revista.fecha_publi}\nNúmero de Edición: {revista.numero_edicion}\nEditorial: {editorial.nombre}\n"
        return HttpResponse(cadenaTxt)
    except Revista.DoesNotExist:
        return HttpResponseNotFound("Revista no encontrada")