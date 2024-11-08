from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('inicio' views.inicio, name='index'),

    path('listadoDeEditoriales/', views.listadoEditoriales, name='lEditoriales'),

    path('listadoDeRevistas/', views.listadoRevistas, name='lRevistas'),

    path('listadoDeProductos/', views.listadoProductos, name='lProductos'), 

    path('editorial/<int:id_editorial>', views.listaDetalleEditorial, name='detalleEditorial'),

    path('revista/<int:id_revista>', views.listaDetalleRevista, name='detalleRevista'),

    path('producto/<int:id_producto>', views.listadoDetallesProdcto, name='detalleProducto')




    path('listadoDeEditoriales/', views.listaEditoriales, name='listaE'),
    path('editoriales/<int:id_editorial>/', views.detalleEDITORIAL, name="detalle"),
]


urlpatterns = [
¡

    #### VER MODELOS AHORA SOLO VIENEN LAS LISTAS

    # /empresaAPP/listadoDeEmpresas/ - Lista de empresas en texto
    path('listadoDeEmpresas/', views.listaEmpresas, name='listaE'),

    # /empresaAPP/listadoDeTrabajadores/ - Lista de trabajadores en texto
    path('listadoDeTrabajadores/', views.listaTrabajadores, name='listat'),

    ### AHORA VIENE EL VER CADA UNO DE LOS MODELOS EN BASE DE DATOS

    # /empresaAPP/empresas/5/ - Detalle de la empresa en texto
    path('empresas/<int:id_empresa>', views.detalleEMPRESA, name='detalle'),

    # /empresaAPP/detalleTrabajador/5/ - Detalle de trabajador en texto
    path('detalleTrabajador/<int:id_trabajador>', views.detalleTrabajador, name='detalleTrabajador'),

    ### VISTAS QUE USAN PLANTILLAS

    # /empresaAPP/listadoDeTrabajadoresConPlantillas/
    path('listadoDeTrabajadoresConPlantillas/', views.listaTrabajadores2, name='listaTrabajadoresPlantillas'),

    # /empresaAPP/detalleTrabajadorConPlantillas/5/
    path('detalleTrabajadorConPlantillas/<int:id_trabajador>', views.detalleTrabajadorConPlantillas, name='detalleTrabajadorPlantillas'),

    # /empresaAPP/listadoDeEmpresasConPlantillas/
    path('listadoDeEmpresasConPlantillas/', views.listaEmpresasConPlantillas, name='listaEmpresasPlantillas'),

    # /empresaAPP/detalleEmpresaConPlantillas/5/
    path('detalleEmpresaConPlantillas/<int:id_empresa>', views.detalleEmpresaConPlantillas, name='detalleEmpresaPlantillas'),
]
