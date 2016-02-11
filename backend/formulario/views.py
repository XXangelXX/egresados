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
    usuario=request.user
    if request.method=='POST':
        siguiente = request.GET.get('siguiente','')

        if siguiente == "actualizar":
            instance = get_object_or_404(PerfilEgresado, num_control=usuario.username)
            fperfil=PerfilEgresadoForm(request.POST, instance=instance)
            if fperfil.is_valid():
                perfil=fperfil.save()
                perfil.usuario=usuario
                perfil.save()
                return Redirect("/egresado/actualizar")
            else:
                print("Datos Incorrectos")
                return Redirect("/egresado/perfil")
        elif siguiente == "nuevo":
            fperfil = PerfilEgresadoForm(request.POST)
            if fperfil.is_valid():
                perfil=fperfil.save()
                perfil.usuario=usuario
                perfil.save()
                return Redirect("/egresado/datoslaborales")
            else:
                print("Datos Incorrectos")
                return render (request, "formulario/actualizar_perfil.html", {"error":"Datos Incorrectos"})
    else:
        try:
            user = PerfilEgresado.objects.get(num_control=usuario.username)
            return render (request, "formulario/actualizar_perfil.html", {"usuario":user, "siguiente":"actualizar"})
        except ObjectDoesNotExist:
            return render (request, "formulario/actualizar_perfil.html", {"siguiente":"nuevo"})
    

# /egresado/datoslaborales
def actualizar_datoslab(request):
    usuario=request.user
    if request.method=='POST':
        siguiente = request.GET.get('siguiente','')

        if siguiente == "actualizar":
            instance = get_object_or_404(DatosLaborales, num_control=usuario.username)
            fperfil=DatosLaboralesForm(request.POST, instance=instance)
            if fperfil.is_valid():
                perfil=fperfil.save()
                perfil.usuario=usuario
                perfil.save()
                return Redirect("/egresado/actualizar")
            else:
                print("Datos Incorrectos")
                return Redirect("/egresado/perfil")
        elif siguiente == "nuevo":
            fperfil = DatosLaboralesForm(request.POST)
            if fperfil.is_valid():
                perfil=fperfil.save()
                perfil.usuario=usuario
                perfil.save()
                return Redirect("/egresado/datoslaborales")
            else:
                print("Datos Incorrectos")
                return render (request, "formulario/actualizar_datoslab.html", {"error":"Datos Incorrectos"})
    else:
        try:
            print usuario.id
            user = DatosLaborales.objects.get(id=usuario.id)
            return render (request, "formulario/actualizar_datoslab.html", {"usuario":user, "siguiente":"actualizar"})
        except ObjectDoesNotExist:
            return render (request, "formulario/actualizar_datoslab.html", {"siguiente":"nuevo"})
    

# /egresado/empresa
def actualizar_empresa(request):
     return render (request, "formulario/actualizar_empresa.html", {})

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
        return HttpResponseRedirect("http://ittehuacan.occ.com.mx/Cuenta/Nueva")
   




# Create your views here.
