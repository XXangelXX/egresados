from django.shortcuts import render
from django.http import HttpResponseRedirect as Redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from .forms import  PerfilEgresadoForm, DatosLaboralesForm, EmpresaForm, EncargadoForm, UserForm
from perfil.models import PerfilEgresado, DatosLaborales
from empresa.models import Empresa, Encargado



def registro (request):
    if request.method=='POST':
        usuario = request.POST.get('username','')
        passwd = request.POST.get('password','')
        if User.objects.filter (username = usuario):
            return render(request, "formulario/registro.html",
                        {"c_registro" : "active",
                         "error": "Numero de control ya esta registrado, intenta iniciar sesion"})
        else:
            if not True:
                return render (request, "formulario/registro.html", 
                    {"c_registro" : "active", "error": "Numero de control mal escrito"})

            else:
                egresado = User.objects.create_user(usuario, None, passwd) 
                if egresado: 
                     return render (request, "formulario/registro.html", 
                    {"c_registro" : "active","modal": usuario})
    else:
        return render (request, "formulario/registro.html", {"c_registro" : "active"})

def encuesta_completa(request):
    pass
# /egresado/actualizar
def actualizar(request):
    return render (request, "formulario/actualizar.html", {})


@login_required(login_url='/')  # /egresado/perfil
def actualizar_perfil(request):
    errors=[]
    usuario=request.user
    if request.method=='POST':
        nuevo=False

        try:
            instance = get_object_or_404(PerfilEgresado, num_control=usuario.username)
            fperfil=PerfilEgresadoForm(request.POST, instance=instance)
        except Exception, e:
            fperfil = PerfilEgresadoForm(request.POST)
            nuevo=True

        titulado = request.POST.get('titulado','')
        print "titulado: %s" % titulado



        if fperfil.is_valid():
            perfil=fperfil.save()
            if titulado:
                perfil.titulado=1
            else:
                perfil.titulado=0
            perfil.usuario=usuario
            perfil.save()
            #return Redirect("/egresado/actualizar")
        else:
            errors.append(fperfil.errors)
            print errors
            print("Datos Incorrectos")
            return render (request, "formulario/actualizar_perfil.html", {"usuario":fperfil})
            #return Redirect("/egresado/perfil")

        if nuevo:
            return Redirect("/egresado/datoslaborales/")
        else:
            return Redirect("/egresado/actualizar")



      
    else:
        try:
            user = PerfilEgresado.objects.get(num_control=usuario.username)
            fperfil=PerfilEgresadoForm( instance=user)
            return render (request, "formulario/actualizar_perfil.html", {"usuario":fperfil})
        except:
            fperfil = PerfilEgresadoForm(request.POST)
            return render (request, "formulario/actualizar_perfil.html",{"usuario":fperfil})
    

# /egresado/datoslaborales
@login_required(login_url='/')
def actualizar_datoslab(request):
    errors=[]
    usuario=request.user
    if request.method=='POST':
        nuevo=False

        try:
            instance = get_object_or_404(DatosLaborales, num_control=usuario.username)
            fperfil=DatosLaboralesForm(request.POST, instance=instance)
        except Exception, e:
            fperfil = DatosLaboralesForm(request.POST)
            nuevo=True


        if fperfil.is_valid():
            fperfil.egresado=usuario
            perfil=fperfil.save()
            perfil.num_control=usuario.username
            perfil.save()
            #return Redirect("/egresado/actualizar")
        else:
            errors.append(fperfil.errors)
            print errors
            print("Datos Incorrectos")
            #return Redirect("/egresado/perfil")
            return render (request, "formulario/actualizar_datoslab.html", {"usuario":fperfil})

        if nuevo:
            return Redirect("/egresado/empresa/")
        else:
            return Redirect("/egresado/actualizar")



      
    else:
        try:
            user = DatosLaborales.objects.get(num_control=usuario.username)
            fperfil=DatosLaboralesForm( instance=user)
            return render (request, "formulario/actualizar_datoslab.html", {"usuario":fperfil})
        except:
            return render (request, "formulario/actualizar_datoslab.html", {"usuario":fperfil})

# /egresado/empresa
@login_required(login_url='/')
def actualizar_empresa(request):
    errors=[]
    usuario=request.user
    if request.method=='POST':
        nuevo=False

        try:
            instance = get_object_or_404(Empresa, num_control=usuario.username)
            fperfil=EmpresaForm(request.POST, instance=instance)
            instance2 = get_object_or_404(Encargado, num_control=usuario.username)
            fperfil2=EncargadoForm(request.POST, instance=instance)
        except Exception, e:
            fperfil = EmpresaForm(request.POST)
            fperfil2 = EncargadoForm(request.POST)
            nuevo=True


        if fperfil.is_valid():
            fperfil.datoslaborales=DatosLaborales.objects.get(num_control=usuario.username)
            perfil=fperfil.save()
            perfil.num_control=usuario.username
            perfil=fperfil.save()

            fperfil2.empresa=Empresa.objects.get(num_control=usuario.username)
            perfil2=fperfil2.save()
            perfil2.num_control=usuario.username            
            perfil2.save()
            
            #return Redirect("/egresado/actualizar")
        else:
            errors.append(fperfil.errors)
            print errors
            print("Datos Incorrectos")
            #return Redirect("/egresado/perfil")
            return render (request, "formulario/actualizar_empresa.html", {"usuario":fperfil, "usuario":fperfil2})

        if nuevo:
            return Redirect("/egresado/gracias/")
        else:
            return Redirect("/egresado/actualizar")



      
    else:
        try:
            user = Empresa.objects.get(num_control=usuario.username)
            fperfil=EmpresaForm( instance=user)
            encargado = Encargado.objects.get(num_control=usuario.username)
            fperfil2=EncargadoForm( instance=user)
            return render (request, "formulario/actualizar_empresa.html", {"usuario":fperfil, "encargado":encargado})
        except:
            return render (request, "formulario/actualizar_empresa.html", {"usuario":fperfil2, "encargado":encargado})

    
def get_encargado(request):
    usuario=request.user
    try:
        encargado=Encargado.objects.get(num_control=usuario.username)
        return encargado
    except Exception, e:
        encargado={}
        return encargado
    


def change_password(request):
    if request.method=='POST':
        passwd = request.POST.get('password','')
        user= request.user
        user.set_password(passwd)
        user.save()
        return HttpResponseRedirect("/")
    else:
        return render (request, "formulario/actualizar_password.html", {})

def ligaocc(request):
    return Redirect("http://ittehuacan.occ.com.mx/Cuenta/Nueva")


def gracias(request):
    usuario=request.user
    usuario = PerfilEgresado.objects.get(num_control=usuario.username)
    return render (request, "formulario/gracias.html", {"usuario":usuario})

