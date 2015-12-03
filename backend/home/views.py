from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.template import RequestContext


# Create your views here.

def index_view(request):
    'pagina principal'
    usuario=request.user
    if usuario.is_anonymous():
        if request.method=='POST':
            #solicitud de login por post
            if True:
                usuariof=request.POST.get('username','')
                clavef=request.POST.get('password','')
                acceso=authenticate(username=usuariof,password=clavef)
                if acceso is not None:
                    if acceso.is_active:
                        login(request,acceso)
                        #Pantalla del Perfil
                        return HttpResponseRedirect('/')
                    else:
                        error="Posiblemente tu usuario este baneado o desactivado, comunicate con el administrador"
                else:
                    error="El usuario no existe, verifique que este bien escrito"
            else:
                error="Datos invalidos en el formulario"
            ctx={'error':error, 'c_login':'active'}
            return render_to_response('home/index.html', ctx,
                          context_instance=RequestContext(request))
        else:
            #Login
            return render_to_response('home/index.html',
                          {'c_login':'active'},
                          context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/home')

from perfil.models import PerfilEgresado
def home(request):
    cxt={}
    if request.method == 'POST':
        filtro_numcontrol = request.POST.get('numcontrol_f','')
        filtro_numcontrol = str(filtro_numcontrol)
        egresado_numcontrol = PerfilEgresado.objects.get(num_control=filtro_numcontrol)
        cxt = {'egresado_numcontrol':egresado_numcontrol}
    return render(request,'home/home.html', cxt)


def carrera(request):
    cxt={}
    if request.method=='POST':
        filtro_carrera=request.POST.get('carrera_f','')
        egresados = PerfilEgresado.objects.filter(carrera=filtro_carrera)
        {'Egresados': egresados, valuecarrera(filtro_carrera): True}
        cxt = {'Egresados': egresados,
                valuecarrera(filtro_carrera): True}
    return render(request,'home/home.html', cxt)

def valuecarrera(carrera):
    carrera  = int(carrera)
    if carrera == 1:
        return "selectbio"
    elif carrera == 2:
        return "selectciv"
    elif carrera == 3:
        return "selectelec"
    elif carrera == 4:
        return "selectind"
    elif carrera == 5:
        return "selectmec"
    elif carrera == 6:
        return "selectsis"
    elif carrera == 7:
        return "selectadm"
    elif carrera == 8:
        return "selectcon"
    elif carrera == 9:
        return "selectelem"
    elif carrera == 10:
        return "selectges"
    elif carrera == 11:
        return "selectlog"
    else:
        return  "selectcarrera"
    
  

def info(request):
    return render(request,'home/info.html', {'nombre':'luis'})


@login_required(login_url='/')
def log_out(request):
    logout(request)
    return HttpResponseRedirect('/')
