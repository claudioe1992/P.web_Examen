from django.shortcuts import render, get_object_or_404
# Create your views here.
from .models import Mecanico, Genero, Producto, Trabajo, Carrito
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import GeneroForm


# Views Taller McQueen
def index(request):
    context={}
    return render(request, 'mecanicos/index.html', context)

def principal(request):
    context={}
    return render(request, 'mecanicos/principal.html', context)

def registros(request):
    mecanicos = Mecanico.objects.all()
    productos = Producto.objects.all()
    trabajos = Trabajo.objects.all()
    return render(request, 'mecanicos/registros.html', {'mecanicos': mecanicos, 'productos': productos, 'trabajos': trabajos})

def nosotros(request):
    context={}
    return render(request, 'mecanicos/nosotros.html', context)


def servicios(request):
    context={}
    return render(request, 'mecanicos/servicios.html', context)


def tienda(request):
    context={}
    return render(request, 'mecanicos/tienda.html', context)


def contacto(request4):
    context={}
    return render(request4, 'mecanicos/contacto.html', context)


def formulario(request):
    context={}
    return render(request, 'mecanicos/formulario.html', context)

def registro(request):
    context={}
    return render(request, 'mecanicos/registro.html', context)

def trabajo1(request):
    context={}
    return render(request, 'mecanicos/trabajo1.html', context)

def trabajo2(request):
    context={}
    return render(request, 'mecanicos/trabajo2.html', context)

def trabajo3(request):
    context={}
    return render(request, 'mecanicos/trabajo3.html', context)

def exito(request):
    context={}
    return render(request, 'mecanicos/exito.html', context)

def iniciar(request):
    context={}
    return render(request, 'mecanicos/iniciar.html', context)

def cargar(request):
    context={}
    return render(request, 'mecanicos/cargar.html', context)

def login(request):
    context={}
    return render(request, 'mecanicos/login.html', context)



# Views CRUD Mecanicos
def mecanicosAdd(request):
    if request.method != "POST":
        generos = Genero.objects.all()
        context = {"generos": generos}
        return render(request, 'mecanicos/mecanicos_add.html', context)
    else:
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        aPaterno = request.POST["paterno"]
        aMaterno = request.POST["materno"]
        fechaNac = request.POST["fechaNac"]
        genero = request.POST["genero"]
        telefono = request.POST["telefono"]
        email = request.POST["email"]
        direccion = request.POST["direccion"]
        
        objGenero = Genero.objects.get(id_genero=genero)
        obj = Mecanico.objects.create(
            rut=rut,
            nombre=nombre,
            apellido_paterno=aPaterno,
            apellido_materno=aMaterno,
            fecha_nacimiento=fechaNac,
            id_genero=objGenero,
            telefono=telefono,
            email=email,
            direccion=direccion,
        )
        obj.save()
        context = {'mensaje': "Ok, datos grabados...", "generos": Genero.objects.all()}
        return render(request, 'mecanicos/mecanicos_add.html', context)


def crud(request):
    mecanicos = Mecanico.objects.all()
    context = {"mecanicos": mecanicos}
    return render(request, 'mecanicos/mecanicos_list.html', context)


def mecanicos_del(request, pk):
    context = {}
    try:
        mecanico = Mecanico.objects.get(rut=pk)
        mecanico.delete()
        mensaje = "Bien, datos eliminados..."
        mecanicos = Mecanico.objects.all()
        context = {'mecanicos': mecanicos, 'mensaje': mensaje}
        return render(request, 'mecanicos/mecanicos_list.html', context)
    except Mecanico.DoesNotExist:
        mensaje = "Error, rut no existe..."
        mecanicos = Mecanico.objects.all()
        context = {'mecanicos': mecanicos, 'mensaje': mensaje}
        return render(request, 'mecanicos/mecanicos_list.html', context)


def mecanicos_findEdit(request, pk):
    if pk != "":
        mecanico = get_object_or_404(Mecanico, rut=pk)
        generos = Genero.objects.all()

        # Formatear la fecha de nacimiento al formato YYYY-MM-DD
        if mecanico.fecha_nacimiento:
            mecanico.fecha_nacimiento = mecanico.fecha_nacimiento.strftime('%Y-%m-%d')

        context = {'mecanico': mecanico, 'generos': generos}
        return render(request, 'mecanicos/mecanicos_edit.html', context)


def mecanicosUpdate(request):
    if request.method == "POST":
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        aPaterno = request.POST["paterno"]
        aMaterno = request.POST["materno"]
        fechaNac = request.POST["fechaNac"]
        genero = request.POST["genero"]
        telefono = request.POST["telefono"]
        email = request.POST["email"]
        direccion = request.POST["direccion"]
        
        objGenero = Genero.objects.get(id_genero=genero)
        mecanico = Mecanico.objects.get(rut=rut)
        mecanico.nombre = nombre
        mecanico.apellido_paterno = aPaterno
        mecanico.apellido_materno = aMaterno
        mecanico.fecha_nacimiento = fechaNac
        mecanico.id_genero = objGenero
        mecanico.telefono = telefono
        mecanico.email = email
        mecanico.direccion = direccion
        mecanico.save()

        context = {'mensaje': "Ok, datos actualizados...", 'mecanico': mecanico, 'generos': Genero.objects.all()}
        return render(request, 'mecanicos/mecanicos_edit.html', context)
    else:
        mecanicos = Mecanico.objects.all()
        context = {'mecanicos': mecanicos}
        return render(request, 'mecanicos/mecanicos_list.html', context)
    

# Views CRUD Generos
def crud_generos(request):
    generos=Genero.objects.all()
    context ={'generos':generos}
    print("enviado datos generos_list")
    return render(request,"mecanicos/generos_list.html",context)


def generosAdd(request):
    print("controlador generosAdd...")
    context={}
    
    if request.method == "POST":
        print("es un POST...")
        form = GeneroForm(request.POST)
        if form.is_valid:
            print("estoy en agr3egar...")
            form.save()
            
            #limpiar form
            form=GeneroForm()
            
            context={'mensaje':"Ok, datos grabados...","form":form}
            return render(request,"mecanicos/generos_add.html",context)
    else:
        form = GeneroForm()
        context={'form':form}
        return render(request, 'mecanicos/generos_add.html',context)
    
    
def generos_del(request, pk):
    mensajes=[]
    errores=[]
    generos = Genero.objects.all()
    try:
        genero = Genero.objects.get(id_genero=pk)
        context={}
        if genero:
            genero.delete()
            mensajes.append("bien, datos eliminados...")
            context = {'generos':generos, 'mensajes': mensajes, 'errores':errores}
            return render(request, 'mecanicos/generos_list.html', context)
    except:
        print("error, id no existe...")
        generos = Genero.objects.all()
        mensaje="error, id no existe"
        context={'mensaje':mensaje, 'generos':generos}
        return render(request, 'mecanicos/generos_list.html', context)


def generos_edit(request, pk):
    try:
        genero=Genero.objects.get(id_genero=pk)
        context={}
        if genero:
            print("edit encontró el genero...")
            if request.method == "POST":
                print("edit, es un POST")
                form = GeneroForm(request.POST, instance=genero)
                form.save()
                mensaje="Bien, datos actualizados..."
                print(mensaje)
                context = {'genero':genero, 'form':form, 'mensaje':mensaje}
                return render(request, 'mecanicos/generos_edit.html', context)
            else:
                #no es un POST
                print("edit, NO es un POST")
                form = GeneroForm(instance=genero)
                mensaje=""
                context = {'genero':genero, 'form':form, 'mensaje':mensaje}
                return render(request, 'mecanicos/generos_edit.html', context)
    except:
        print("error, id no existe...")
        generos=Genero.objects.all()
        mensaje="Error, id no existe"
        context={'mensaje':mensaje, 'generos':generos}
        return render(request, 'mecanicos/generos_edit.html', context)


@login_required
def menu(request):
    #Irrelevante
    request.session["usuario"]="martinjara.duoc"
    usuario=request.session["usuario"]
    context = {'usuario':usuario}
    return render(request, '', context)

