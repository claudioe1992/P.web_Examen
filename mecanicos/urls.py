#from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    # URLs Taller McQueen.
    path('', views.index, name='index'),
    path('principal.html', views.principal, name='principal'),
    path('index.html', views.index, name='index'),
    path('registros.html', views.registros, name='registros'),
    path('principal.html', views.registros, name='registros'),
    path('nosotros.html', views.nosotros, name='nosotros'),
    path('servicios.html', views.servicios, name='servicios'),
    path('tienda.html', views.tienda, name='tienda'),
    path('contacto.html', views.contacto, name='contacto'),
    path('formulario.html', views.formulario, name='formulario'),
    path('login.html', views.login, name="login"),
    
    # URLs Spinner JS
    path('iniciar.html', views.iniciar, name='iniciar'),
    path('cargar.html', views.cargar, name='cargar'),
    path('registro.html', views.registro, name='registro'),
    path("exito.html", views.exito, name="exito"),
    
    path('trabajo1.html', views.trabajo1, name='trabajo1'),
    path('trabajo2.html', views.trabajo2, name='trabajo2'),
    path('trabajo3.html', views.trabajo3, name='trabajo3'),
    
    path('mecanicosAdd', views.mecanicosAdd, name='mecanicosAdd'),
    path('crud', views.crud, name='crud'),
    path('mecanicos_del/<str:pk>', views.mecanicos_del, name='mecanicos_del'),
    path('mecanicos_findEdit/<str:pk>', views.mecanicos_findEdit, name='mecanicos_findEdit'),
    path('mecanicosUpdate', views.mecanicosUpdate, name='mecanicosUpdate'),
    
    path('crud_generos', views.crud_generos, name='crud_generos'),
    path('generosAdd', views.generosAdd, name='generosAdd'),
    path('generos_del/<str:pk>', views.generos_del, name='generos_del'),
    path('generos_edit/<str:pk>', views.generos_edit, name='generos_edit'),
]
