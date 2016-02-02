from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User


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

# /egresado/perfil
def actualizar_perfil(request):
     return render (request, "formulario/actualizar_perfil.html", {})

# /egresado/datoslaborales
def actualizar_datoslab(request):
     return render (request, "formulario/actualizar_datoslab.html", {})

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
